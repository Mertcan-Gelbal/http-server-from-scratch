# Katkıda Bulunma Rehberi

HTTP Web Sunucusu projesine katkıda bulunduğunuz için teşekkür ederiz!

## Nasıl Katkıda Bulunabilirsiniz

### 1. Issue Bildirme
- Hata bulduğunuzda veya yeni özellik önerileriniz olduğunda issue açın
- Mümkün olduğunca detaylı bilgi verin
- Hata raporlarında sistem bilgilerinizi ve hata mesajlarını ekleyin

### 2. Pull Request Gönderme
1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi yapın
4. Commit mesajlarınızı açıklayıcı yazın
5. Pull request gönderin

### 3. Kod Standartları
- Python PEP 8 standartlarına uyun
- Fonksiyonlarınızı dokümante edin
- Anlamlı değişken isimleri kullanın
- Türkçe yorum satırları ekleyin

## Geliştirme Süreci

### Kurulum
```bash
git clone https://github.com/kullanici/http-server-from-scratch.git
cd http-server-from-scratch
python server.py
```

### Test Etme
```bash
# Sunucuyu başlat
python server.py

# Başka bir terminalde test et
curl http://localhost:8080/api/hello
```

### Docker ile Test
```bash
docker build -t http-server-test .
docker run -p 8080:8080 http-server-test
```

## Katkı Alanları

### Öncelikli Geliştirmeler
- HTTPS desteği
- WebSocket implementasyonu
- Daha gelişmiş routing sistemi
- Template engine entegrasyonu
- Session yönetimi
- Rate limiting
- Caching mekanizması

### Dokümantasyon
- API dokümantasyonu
- Kod örnekleri
- Video tutorials
- Performans testleri

### Test Coverage
- Unit testler
- Integration testler
- Load testler
- Security testler

## Kod Örnekleri

### Yeni Endpoint Ekleme
```python
def handle_api_new_endpoint(self, request_data):
    """Yeni API endpoint"""
    response_data = {
        "message": "Yeni endpoint çalışıyor",
        "timestamp": datetime.now().isoformat()
    }
    return self.create_json_response(response_data)

# Route'u kaydet
self.routes['/api/new'] = self.handle_api_new_endpoint
```

### Middleware Ekleme
```python
def middleware_auth(self, request_data):
    """Kimlik doğrulama middleware'i"""
    # Auth logic here
    return True
```

## Commit Mesaj Formatı

```
tip(kapsam): kısa açıklama

Detaylı açıklama (isteğe bağlı)

Fixes #123
```

### Tip Örnekleri:
- `feat`: Yeni özellik
- `fix`: Hata düzeltmesi
- `docs`: Dokümantasyon
- `style`: Kod formatı
- `refactor`: Kod yeniden düzenleme
- `test`: Test ekleme
- `chore`: Bakım işleri

## Release Süreci

1. Version numarasını güncelle
2. CHANGELOG.md dosyasını güncelle
3. Tag oluştur (`git tag v1.0.0`)
4. Docker image'ı build et ve push et
5. GitHub release oluştur

## İletişim

- **Geliştirici**: Mertcan Gelbal
- **Email**: mertcan@example.com
- **GitHub**: @mertcangelbal

## Teşekkürler

Tüm katkıda bulunanlar:
- Mertcan Gelbal (@mertcangelbal) - Ana geliştirici

---

Bu proje eğitim amaçlı geliştirilmiştir. Katkılarınız öğrenme sürecimize büyük değer katmaktadır! 