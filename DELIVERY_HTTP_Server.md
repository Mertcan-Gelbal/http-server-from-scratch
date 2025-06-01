# HTTP Web Sunucusu Ödevi Teslim Raporu

## Öğrenci Bilgileri
- **Ad Soyad**: Mertcan Gelbal
- **Öğrenci Numarası**: 171421012

---

## GitHub Repository Linki
https://github.com/Mertcan-Gelbal/http-server-from-scratch

---

## Proje Açıklaması
Sıfırdan geliştirilmiş, tam özellikli HTTP web sunucusu uygulamasıdır. 
Uygulama şu özellikleri desteklemektedir:

### Temel Özellikler:
- TCP socket üzerinden `GET` istekleri
- `/static` dizininden dosya sunumu (HTML, CSS, JS)
- `/api/hello`, `/api/time`, `/api/status` endpoint'lerinden JSON döndürme
- MIME type yönetimi (Content-Type header'ları)
- HTTP hata yanıtları (404, 500, 405, 403)

### Gelişmiş Özellikler (Bonus):
- Çoklu bağlantı desteği (Threading)
- `POST` isteği işleme (`/api/echo` endpoint)
- Kapsamlı loglama sistemi (dosya + konsol)
- Route handler yapısı (Flask benzeri)
- Güvenlik kontrolleri (Directory traversal koruması)
- Interaktif test arayüzü
- Ana sayfa ile proje tanıtımı

---

## Docker Container Bilgileri

### Docker Hub Image Linki
https://hub.docker.com/repository/docker/gelbalmertcan/http-server-from-scratch

### Container Açıklaması
Proje aşağıdaki Dockerfile kullanılarak container haline getirilmiştir.  
Sunucu 8080 portu üzerinden dış dünyaya servis sağlamaktadır.

**Base Image**: `python:3.11-slim`
**Exposed Port**: 8080
**Health Check**: Dahili sağlık kontrolü

### Komutlar:
```bash
# Docker image oluştur
docker build -t gelbalmertcan/http-server-from-scratch .

# Container'ı çalıştır
docker run -p 8080:8080 gelbalmertcan/http-server-from-scratch

# Docker Hub'dan çek ve çalıştır
docker run -p 8080:8080 gelbalmertcan/http-server-from-scratch:latest

# Docker Compose ile çalıştır
docker-compose up -d

# Docker Hub'a push et
docker push gelbalmertcan/http-server-from-scratch:latest
```

**Ek Özellikler**:
- `compose.yaml` dosyası ile çoklu servis yapılandırması
- Volume mapping (log dosyaları için)
- Network yapılandırması
- Health check ve restart policy

---

## Açık Kaynak Yapı Dosyaları

| Dosya Adı            | Açıklama                                        |
|----------------------|-------------------------------------------------|
| `README.md`          | Proje tanıtımı, kurulum ve çalıştırma yönergesi |
| `LICENSE`            | MIT Lisans metni                                    |
| `CONTRIBUTING.md`    | Katkı kuralları ve geliştirme rehberi                                 |
| `NOTICE.md`          | Üçüncü parti lisanslar ve bildirimler                  |
| `CODE_OF_CONDUCT.md` | Topluluk davranış kuralları                     |
| `Dockerfile`         | Container yapılandırma dosyası                  |
| `compose.yaml`       | Docker Compose çoklu servis yapılandırması             |
| `.dockerignore`      | Docker build dışı bırakılan dosyalar            |

---

## Proje Yapısı

```
/
├── server.py              # Ana HTTP sunucu kodu (368 satır)
├── static/                # Statik dosyalar dizini
│   ├── test.html         # Interaktif test sayfası
│   ├── style.css         # Modern CSS tasarımı
│   └── script.js         # JavaScript test fonksiyonları
├── Dockerfile            # Docker yapılandırması
├── compose.yaml          # Docker Compose yapılandırması
├── .dockerignore         # Docker ignore dosyası
├── README.md             # Kapsamlı proje dokümantasyonu
├── LICENSE               # MIT Lisans
├── CONTRIBUTING.md       # Katkı kuralları
├── NOTICE.md             # Üçüncü parti lisanslar
└── CODE_OF_CONDUCT.md    # Davranış kuralları
```

---

## Test Edilebilir Özellikler

### API Endpoints:
- `GET /` - Ana sayfa (HTML)
- `GET /api/hello` - Merhaba mesajı (JSON)
- `GET /api/time` - Güncel zaman (JSON)
- `GET /api/status` - Sunucu durumu (JSON)
- `POST /api/echo` - Echo servisi (JSON)

### Statik Dosyalar:
- `GET /static/test.html` - Test sayfası
- `GET /static/style.css` - CSS dosyası
- `GET /static/script.js` - JavaScript dosyası

### Test Komutları:
```bash
# API testleri
curl http://localhost:8080/api/hello
curl http://localhost:8080/api/time
curl http://localhost:8080/api/status
curl -X POST http://localhost:8080/api/echo -d "test data"

# Statik dosya testi
curl http://localhost:8080/static/test.html
```

---

## Teknik Detaylar

### Kullanılan Teknolojiler:
- **Python 3.11**: Ana programlama dili
- **Socket Programming**: TCP bağlantıları
- **Threading**: Çoklu bağlantı desteği
- **Docker**: Containerization
- **HTML5/CSS3/JavaScript**: Web arayüzü

### Güvenlik Özellikleri:
- Directory traversal koruması
- Input validation
- Error handling
- Secure headers

### Performans Özellikleri:
- Asenkron bağlantı işleme
- Efficient file serving
- Memory optimization
- Comprehensive logging

---

## Ek Notlar

Bu proje tamamen sıfırdan geliştirilmiştir ve hiçbir üst seviye framework (Flask, Express vb.) kullanılmamıştır. Sadece Python'un standart kütüphaneleri kullanılarak socket programlama ile HTTP protokolü implement edilmiştir.

Proje eğitim amaçlı geliştirilmiş olup, HTTP protokolü, socket programlama, Docker containerization ve açık kaynak geliştirme süreçlerini kapsamlı bir şekilde örneklemektedir.

**Geliştirme Süresi**: ~8 saat
**Kod Satırı**: 368 satır (Python) + 200+ satır (HTML/CSS/JS)
**Test Durumu**: Tüm özellikler test edilmiş ve çalışır durumda
