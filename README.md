# HTTP Web Sunucusu

Sıfırdan geliştirilmiş, tam özellikli HTTP web sunucusu implementasyonu.

## Geliştirici Bilgileri
- **Ad Soyad**: Mertcan Gelbal
- **Öğrenci Numarası**: 171421012

## Proje Açıklaması

Bu proje, Python socket programlama kullanarak sıfırdan geliştirilmiş bir HTTP web sunucusudur. Framework kullanmadan, temel TCP socket'ler üzerinden HTTP protokolünü implement eder.

## Özellikler

### Temel Özellikler
- TCP socket üzerinden HTTP GET istekleri
- Statik dosya sunumu (`/static` dizini)
- JSON API endpoints
- MIME type yönetimi
- HTTP hata yanıtları (404, 500, vb.)

### Gelişmiş Özellikler
- Çoklu bağlantı desteği (Threading)
- POST istekleri
- Kapsamlı loglama sistemi
- Route handler yapısı
- Güvenlik kontrolleri (Directory traversal koruması)
- Docker containerization
- Health check desteği

## Kurulum

### Gereksinimler
- Python 3.7+
- Docker (opsiyonel)

### Yerel Kurulum
```bash
# Repoyu klonla
git clone https://github.com/Mertcan-Gelbal/http-server-from-scratch.git
cd http-server-from-scratch

# Sunucuyu başlat
python server.py
```

### Docker ile Kurulum
```bash
# Docker image oluştur
docker build -t gelbalmertcan/http-server-from-scratch .

# Container'ı çalıştır
docker run -p 8080:8080 gelbalmertcan/http-server-from-scratch

# Docker Hub'dan direkt çalıştır
docker run -p 8080:8080 gelbalmertcan/http-server-from-scratch:latest
```

### Docker Compose ile Kurulum
```bash
# Servisleri başlat
docker-compose up -d

# Logları görüntüle
docker-compose logs -f
```

## Kullanım

Sunucu başlatıldıktan sonra aşağıdaki URL'lere erişebilirsiniz:

### Ana Sayfa
- `http://localhost:8080/` - Ana sayfa

### API Endpoints
- `GET http://localhost:8080/api/hello` - Merhaba mesajı
- `GET http://localhost:8080/api/time` - Güncel zaman
- `GET http://localhost:8080/api/status` - Sunucu durumu
- `POST http://localhost:8080/api/echo` - Echo servisi

### Statik Dosyalar
- `http://localhost:8080/static/test.html` - Test sayfası
- `http://localhost:8080/static/style.css` - CSS dosyası
- `http://localhost:8080/static/script.js` - JavaScript dosyası

## Proje Yapısı

```
/
├── server.py              # Ana HTTP sunucu kodu
├── static/                # Statik dosyalar
│   ├── test.html         # Test HTML sayfası
│   ├── style.css         # CSS dosyası
│   └── script.js         # JavaScript dosyası
├── Dockerfile            # Docker yapılandırması
├── compose.yaml          # Docker Compose yapılandırması
├── .dockerignore         # Docker ignore dosyası
├── README.md             # Bu dosya
├── LICENSE               # Lisans dosyası
├── CONTRIBUTING.md       # Katkı kuralları
├── NOTICE.md             # Üçüncü parti lisanslar
└── CODE_OF_CONDUCT.md    # Davranış kuralları
```

## Test Etme

### Manuel Test
```bash
# GET isteği
curl http://localhost:8080/api/hello

# POST isteği
curl -X POST http://localhost:8080/api/echo -d "test data"

# Statik dosya
curl http://localhost:8080/static/test.html
```

### Web Arayüzü ile Test
`http://localhost:8080/static/test.html` adresine giderek interaktif test arayüzünü kullanabilirsiniz.

## Performans Özellikleri

- **Çoklu bağlantı**: Threading ile eşzamanlı istek işleme
- **Bellek kullanımı**: Optimize edilmiş dosya okuma
- **Güvenlik**: Directory traversal koruması
- **Loglama**: Detaylı istek/yanıt logları

## Docker Bilgileri

### Image Özellikleri
- **Base Image**: python:3.11-slim
- **Port**: 8080
- **Health Check**: Dahili
- **Volume**: Log dosyaları için
- **Docker Hub**: https://hub.docker.com/repository/docker/gelbalmertcan/http-server-from-scratch

### Komutlar
```bash
# Build
docker build -t gelbalmertcan/http-server-from-scratch .

# Run
docker run -p 8080:8080 mertcangelbal/http-server-from-scratch

# Compose
docker-compose up -d
```

## Yapılandırma

Sunucu yapılandırması `server.py` dosyasında değiştirilebilir:

```python
# Sunucu ayarları
HOST = '0.0.0.0'  # Tüm arayüzlerde dinle
PORT = 8080       # Port numarası
```

## Loglama

Sunucu aşağıdaki log seviyelerini destekler:
- **INFO**: Genel bilgiler
- **ERROR**: Hata mesajları
- **DEBUG**: Detaylı debug bilgileri

Log dosyası: `server.log`

## Katkıda Bulunma

Katkıda bulunmak için lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Sonuç

Bu proje eğitim amaçlı geliştirilmiştir ve HTTP protokolü ile socket programlama konularında pratik yapmak için tasarlanmıştır.

---

**Geliştirici**: Mertcan Gelbal | **Öğrenci No**: 171421012 