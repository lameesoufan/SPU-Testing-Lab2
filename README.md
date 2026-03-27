# Calculator Project

تطبيق حاسبة بسيط لتطبيق مفاهيم Software Testing و CI/CD.

## الملفات

| الملف | الوصف |
|-------|-------|
| `calculator.py` | الكود الرئيسي (جمع، طرح، ضرب، قسمة) |
| `test_calculator.py` | اختبارات pytest |
| `.github/workflows/ci.yml` | GitHub Actions Pipeline |

## تشغيل الاختبارات محلياً

pip install pytest
pytest test_calculator.py -v

## Pipeline Flow

Push to main
  → Checkout Code
  → Setup Python
  → Install pytest
  → Run Tests ✅
  → GitLeaks Scan 🔒
  → Build 🔨
  → Deploy 🚀
