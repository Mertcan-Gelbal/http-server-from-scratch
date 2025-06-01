// HTTP Sunucusu Test JavaScript

// API test fonksiyonu
async function testAPI() {
    const resultDiv = document.getElementById('api-result');
    resultDiv.innerHTML = 'API test ediliyor...';
    
    try {
        const response = await fetch('/api/hello');
        const data = await response.json();
        
        resultDiv.innerHTML = `API Test Başarılı!\n\n${JSON.stringify(data, null, 2)}`;
        resultDiv.style.borderLeftColor = '#27ae60';
    } catch (error) {
        resultDiv.innerHTML = `API Test Hatası:\n\n${error.message}`;
        resultDiv.style.borderLeftColor = '#e74c3c';
    }
}

// POST test fonksiyonu
async function testPOST() {
    const resultDiv = document.getElementById('post-result');
    const postData = document.getElementById('post-data').value;
    
    if (!postData.trim()) {
        resultDiv.innerHTML = 'Lütfen test verisi girin!';
        resultDiv.style.borderLeftColor = '#f39c12';
        return;
    }
    
    resultDiv.innerHTML = 'POST isteği gönderiliyor...';
    
    try {
        const response = await fetch('/api/echo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: postData
        });
        
        const data = await response.json();
        
        resultDiv.innerHTML = `POST Test Başarılı!\n\n${JSON.stringify(data, null, 2)}`;
        resultDiv.style.borderLeftColor = '#27ae60';
    } catch (error) {
        resultDiv.innerHTML = `POST Test Hatası:\n\n${error.message}`;
        resultDiv.style.borderLeftColor = '#e74c3c';
    }
}

// Sayfa yüklendiğinde çalışacak fonksiyonlar
document.addEventListener('DOMContentLoaded', function() {
    console.log('HTTP Sunucusu Test Sayfası Yüklendi');
    console.log('Geliştirici: Mertcan Gelbal');
    console.log('Öğrenci No: 171421012');
    
    // Enter tuşu ile POST gönderme
    document.getElementById('post-data').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            testPOST();
        }
    });
    
    // Otomatik API testi (sayfa yüklendiğinde)
    setTimeout(() => {
        console.log('Otomatik API testi başlatılıyor...');
        testAPI();
    }, 1000);
});

// Ek yardımcı fonksiyonlar
function clearResults() {
    document.getElementById('api-result').innerHTML = '';
    document.getElementById('post-result').innerHTML = '';
}

function testAllEndpoints() {
    const endpoints = ['/api/hello', '/api/time', '/api/status'];
    
    endpoints.forEach(async (endpoint, index) => {
        setTimeout(async () => {
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                console.log(`${endpoint} yanıtı:`, data);
            } catch (error) {
                console.error(`${endpoint} hatası:`, error);
            }
        }, index * 1000);
    });
} 