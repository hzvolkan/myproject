# myproject

![Codecov](https://codecov.io/gh/hzvolkan/myproject/branch/main/graph/badge.svg)

Bu proje, Django ve PostgreSQL kullanılarak geliştirilmiş bir projedir.

## Kurulum

1. **Python bağımlılıklarını yüklemek için:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Veritabanını ayarlamak için:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Testleri çalıştırmak ve kapsam raporu oluşturmak için:**
   ```bash
   coverage run --source='.' manage.py test
   coverage xml
   ```

## CI/CD Pipeline
- **GitHub Actions** entegre edilmiştir.
- **Codecov entegrasyonu** ile test kapsamı ölçülmektedir.

---
