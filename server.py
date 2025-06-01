#!/usr/bin/env python3
"""
HTTP Web Sunucusu - Sıfırdan Geliştirilmiş
Mertcan Gelbal - 171421012
"""

import socket
import threading
import os
import json
import mimetypes
import urllib.parse
from datetime import datetime
import logging

# Loglama yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    ]
)

class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.socket = None
        self.routes = {}
        self.static_dir = 'static'
        
        # Varsayılan route'ları kaydet
        self.register_default_routes()
        
    def register_default_routes(self):
        """Varsayılan API route'larını kaydet"""
        self.routes['/api/hello'] = self.handle_api_hello
        self.routes['/api/time'] = self.handle_api_time
        self.routes['/api/status'] = self.handle_api_status
        
    def handle_api_hello(self, request_data):
        """Hello API endpoint"""
        response_data = {
            "message": "Merhaba! HTTP Sunucusu çalışıyor.",
            "server": "Custom HTTP Server",
            "developer": "Mertcan Gelbal",
            "student_id": "171421012",
            "timestamp": datetime.now().isoformat()
        }
        return self.create_json_response(response_data)
        
    def handle_api_time(self, request_data):
        """Zaman API endpoint"""
        response_data = {
            "current_time": datetime.now().isoformat(),
            "timezone": "UTC+3",
            "unix_timestamp": int(datetime.now().timestamp())
        }
        return self.create_json_response(response_data)
        
    def handle_api_status(self, request_data):
        """Sunucu durumu API endpoint"""
        response_data = {
            "status": "running",
            "server_info": {
                "host": self.host,
                "port": self.port,
                "static_directory": self.static_dir
            },
            "endpoints": list(self.routes.keys())
        }
        return self.create_json_response(response_data)
    
    def start(self):
        """Sunucuyu başlat"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            
            logging.info(f"HTTP Sunucusu başlatıldı: http://{self.host}:{self.port}")
            logging.info(f"Statik dosyalar: /{self.static_dir}")
            logging.info(f"API Endpoints: {list(self.routes.keys())}")
            
            while True:
                client_socket, client_address = self.socket.accept()
                logging.info(f"Yeni bağlantı: {client_address}")
                
                # Her bağlantı için ayrı thread
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.daemon = True
                client_thread.start()
                
        except KeyboardInterrupt:
            logging.info("Sunucu kapatılıyor...")
        except Exception as e:
            logging.error(f"Sunucu hatası: {e}")
        finally:
            if self.socket:
                self.socket.close()
    
    def handle_client(self, client_socket, client_address):
        """İstemci bağlantısını işle"""
        try:
            # HTTP isteğini al
            request_data = client_socket.recv(4096).decode('utf-8')
            
            if not request_data:
                return
                
            logging.info(f"İstek alındı: {client_address}")
            
            # HTTP isteğini parse et
            request_lines = request_data.split('\n')
            request_line = request_lines[0].strip()
            
            if not request_line:
                return
                
            method, path, version = request_line.split(' ')
            
            # URL decode
            path = urllib.parse.unquote(path)
            
            logging.info(f"{method} {path} - {client_address[0]}")
            
            # İsteği işle
            if method == 'GET':
                response = self.handle_get_request(path, request_data)
            elif method == 'POST':
                response = self.handle_post_request(path, request_data)
            else:
                response = self.create_error_response(405, "Method Not Allowed")
            
            # Yanıtı gönder
            client_socket.send(response.encode('utf-8'))
            
        except Exception as e:
            logging.error(f"İstemci işleme hatası: {e}")
            error_response = self.create_error_response(500, "Internal Server Error")
            try:
                client_socket.send(error_response.encode('utf-8'))
            except:
                pass
        finally:
            client_socket.close()
    
    def handle_get_request(self, path, request_data):
        """GET isteklerini işle"""
        # API route kontrolü
        if path in self.routes:
            return self.routes[path](request_data)
        
        # Statik dosya kontrolü
        if path.startswith('/static/'):
            return self.serve_static_file(path)
        
        # Ana sayfa
        if path == '/' or path == '':
            return self.serve_index_page()
        
        # 404 Not Found
        return self.create_error_response(404, "Not Found")
    
    def handle_post_request(self, path, request_data):
        """POST isteklerini işle"""
        if path == '/api/echo':
            return self.handle_api_echo(request_data)
        
        return self.create_error_response(404, "Not Found")
    
    def handle_api_echo(self, request_data):
        """Echo API endpoint - POST verilerini geri döndür"""
        try:
            # POST body'sini al
            body_start = request_data.find('\r\n\r\n')
            if body_start != -1:
                body = request_data[body_start + 4:]
            else:
                body = ""
            
            response_data = {
                "method": "POST",
                "endpoint": "/api/echo",
                "received_data": body,
                "timestamp": datetime.now().isoformat()
            }
            return self.create_json_response(response_data)
        except Exception as e:
            return self.create_error_response(500, f"Echo error: {str(e)}")
    
    def serve_static_file(self, path):
        """Statik dosyaları sun"""
        try:
            # /static/ prefix'ini kaldır
            file_path = path[8:]  # '/static/' = 8 karakter
            full_path = os.path.join(self.static_dir, file_path)
            
            # Güvenlik kontrolü - directory traversal saldırılarını önle
            if '..' in file_path or file_path.startswith('/'):
                return self.create_error_response(403, "Forbidden")
            
            if not os.path.exists(full_path) or not os.path.isfile(full_path):
                return self.create_error_response(404, "File Not Found")
            
            # Dosyayı oku
            with open(full_path, 'rb') as f:
                content = f.read()
            
            # MIME type belirle
            mime_type, _ = mimetypes.guess_type(full_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            
            # HTTP yanıtı oluştur
            response = f"HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: {mime_type}\r\n"
            response += f"Content-Length: {len(content)}\r\n"
            response += f"Server: Custom-HTTP-Server/1.0\r\n"
            response += "\r\n"
            
            # Binary content için bytes olarak döndür
            return response.encode('utf-8') + content
            
        except Exception as e:
            logging.error(f"Statik dosya hatası: {e}")
            return self.create_error_response(500, "Internal Server Error")
    
    def serve_index_page(self):
        """Ana sayfa HTML'ini sun"""
        html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTTP Sunucusu - Mertcan Gelbal</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .section { background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .endpoint { background: #e9ecef; padding: 10px; margin: 5px 0; border-radius: 3px; }
        a { color: #3498db; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="header">
        <h1>HTTP Web Sunucusu</h1>
        <p>Sıfırdan geliştirilmiş HTTP sunucusu</p>
        <p><strong>Geliştirici:</strong> Mertcan Gelbal | <strong>Öğrenci No:</strong> 171421012</p>
    </div>
    
    <div class="section">
        <h2>API Endpoints</h2>
        <div class="endpoint">
            <strong>GET</strong> <a href="/api/hello">/api/hello</a> - Merhaba mesajı
        </div>
        <div class="endpoint">
            <strong>GET</strong> <a href="/api/time">/api/time</a> - Güncel zaman
        </div>
        <div class="endpoint">
            <strong>GET</strong> <a href="/api/status">/api/status</a> - Sunucu durumu
        </div>
        <div class="endpoint">
            <strong>POST</strong> /api/echo - Gönderilen veriyi geri döndür
        </div>
    </div>
    
    <div class="section">
        <h2>Statik Dosyalar</h2>
        <p>Statik dosyalar <code>/static/</code> dizini altında sunulmaktadır.</p>
        <div class="endpoint">
            <a href="/static/test.html">test.html</a> - Test HTML dosyası
        </div>
        <div class="endpoint">
            <a href="/static/style.css">style.css</a> - CSS dosyası
        </div>
        <div class="endpoint">
            <a href="/static/script.js">script.js</a> - JavaScript dosyası
        </div>
    </div>
    
    <div class="section">
        <h2>Özellikler</h2>
        <ul>
            <li>TCP Socket programlama</li>
            <li>HTTP GET ve POST istekleri</li>
            <li>Statik dosya sunumu</li>
            <li>JSON API endpoints</li>
            <li>MIME type desteği</li>
            <li>Çoklu bağlantı (Threading)</li>
            <li>Loglama sistemi</li>
            <li>Hata yönetimi</li>
        </ul>
    </div>
</body>
</html>"""
        
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
        response += "Server: Custom-HTTP-Server/1.0\r\n"
        response += "\r\n"
        response += html_content
        
        return response
    
    def create_json_response(self, data):
        """JSON yanıtı oluştur"""
        json_content = json.dumps(data, ensure_ascii=False, indent=2)
        
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: application/json; charset=utf-8\r\n"
        response += f"Content-Length: {len(json_content.encode('utf-8'))}\r\n"
        response += "Server: Custom-HTTP-Server/1.0\r\n"
        response += "Access-Control-Allow-Origin: *\r\n"
        response += "\r\n"
        response += json_content
        
        return response
    
    def create_error_response(self, status_code, message):
        """Hata yanıtı oluştur"""
        status_messages = {
            400: "Bad Request",
            403: "Forbidden", 
            404: "Not Found",
            405: "Method Not Allowed",
            500: "Internal Server Error"
        }
        
        status_text = status_messages.get(status_code, "Error")
        
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{status_code} {status_text}</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
        .error {{ color: #e74c3c; }}
    </style>
</head>
<body>
    <h1 class="error">{status_code} {status_text}</h1>
    <p>{message}</p>
    <hr>
    <p><small>Custom HTTP Server - Mertcan Gelbal</small></p>
</body>
</html>"""
        
        response = f"HTTP/1.1 {status_code} {status_text}\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
        response += "Server: Custom-HTTP-Server/1.0\r\n"
        response += "\r\n"
        response += html_content
        
        return response

if __name__ == "__main__":
    server = HTTPServer()
    server.start() 