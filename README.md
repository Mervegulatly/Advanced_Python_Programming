Bu repo; Python ile veritabanı (SQLite), dosya okuma/yazma (CSV/JSON), veri sorgulama ve API’den veri çekme gibi konuları içeren örnek çalışmaları barındırır.

## Genel İçerik
- **Hafta 1:** Python temelleri (fonksiyonlar, lambda, koleksiyonlar, filtreleme/sıralama vb.)
- **Hafta 2:** Nesne yönelimli programlama (class/constructor, encapsulation, inheritance, polymorphism vb.)
- **Hafta 3:** Dosya işlemleri (CSV/JSON) + SQLite ile CRUD ve sorgular (Hafta3/Day2 part2)
- **Final_Project:** API’den döviz kurları çekme → SQLite’a kaydetme → sorgulama

---

## Final_Project - Döviz Kurları (API → SQLite)

Bu proje, exchangerate-api.com üzerinden döviz kurlarını çekip seçilen para birimlerini SQLite veritabanına kaydeder ve örnek sorguları ekrana basar.

### Dosyalar
- `Final_Project/request.py`: API’den kurları çeker, sadece `USD`, `EUR`, `GBP` için `secilen_kurlar` dict’ini oluşturur.
- `Final_Project/insert.py`: `secilen_kurlar` içindeki değerleri `Final_Project/final_db.db` üzerindeki `kayitlar` tablosuna yazar.
- `Final_Project/db_queries.py`: `kayitlar` tablosu üzerinde örnek SQL sorgularını çalıştırır.
- `Final_Project/DataPipeLine_App.py`: Tüm akışı çalıştıran dosya (API çekme + tablo/insert + sorgu).

### Gereksinimler
- Python 3.x
- `requests`

Kurulum:
```bash
pip install requests
```

### Çalıştırma
```bash
python Final_Project\DataPipeLine_App.py
```

Alternatif (ayrı ayrı):
```bash
python Final_Project\request.py
python Final_Project\insert.py
python Final_Project\db_queries.py
```

### Veritabanı
- Dosya: `Final_Project/final_db.db`
- Tablo: `kayitlar`
  - `id` (PRIMARY KEY)
  - `birim_adi` (TEXT)
  - `deger` (REAL)
  - `islem_tarihi` (TEXT)

### Seçilen Kurlar
`Final_Project/request.py` içindeki filtre: `USD`, `EUR`, `GBP`.

