# bajarvol loyihasi 

[![GitHub Repo](https://img.shields.io/badge/GitHub-aabdurakhmanov-blue?style=flat&logo=github)](https://github.com/aabdurakhmanov)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](#license)
[![Uzbek TTS](https://img.shields.io/badge/Language-Uzbek-blueviolet?style=flat)](#features)


## ℹ️ Loyihaning qisqacha ta’rifi (About the Project)
Bu loyiha **Django Rest Framework** asosida foydalanuvchi autentifikatsiyasi va profil boshqaruvi uchun yaratilgan.  
Unda **JWT autentifikatsiya**, **email tasdiqlash**, **profil boshqaruvi**, **Google reCAPTCHA**, hamda **API dokumentatsiya** (Swagger & Redoc) mavjud.  

_This project is built with **Django Rest Framework** for user authentication and profile management.  
It includes **JWT authentication**, **email verification**, **profile management**, **Google reCAPTCHA**, and **API documentation** (Swagger & Redoc)._  

---

## 🛠 Texnologiyalar (Technologies Used)
- 🐍 **Python 3.10+**  
- 🎯 **Django 5+**  
- ⚡ **Django Rest Framework (DRF)**  
- 🔐 **JWT (SimpleJWT)**  
- 🔑 **django-recaptcha**  
- 📖 **drf-spectacular & drf-spectacular-sidecar**  
- 🧾 **django-extensions**  

---

## ✨ Imkoniyatlar (Features)

### 👤 Foydalanuvchilar uchun (For Users):
- 📝 Ro‘yxatdan o‘tish (Register) – yangi foydalanuvchi akkaunt yaratishi mumkin  
  _Register a new user account_
- 🔑 Login / Logout – JWT orqali xavfsiz kirish va chiqish  
  _Secure login and logout with JWT authentication_
- 📧 Email tasdiqlash – foydalanuvchilar faqat email tasdiqlangandan keyin aktiv bo‘ladi  
  _Users must verify their email before activation_
- 🔒 Parol himoyasi – parolni mustahkamligi tekshirilib, xavfsiz saqlanadi  
  _Passwords are validated and stored securely_
- 👨‍💻 Profil boshqaruvi – foydalanuvchi o‘z profil ma’lumotlarini yangilay oladi  
  _Users can manage and update their profiles_

---

### 🔐 Xavfsizlik (Security):
- ✅ Google reCAPTCHA – botlardan himoya  
  _Protection against bots using Google reCAPTCHA_
- 🔑 JWT Authentication – login sessiyasiz xavfsiz token asosida amalga oshiriladi  
  _Token-based authentication without sessions_
- 🚫 Token blacklist – chiqib ketgan foydalanuvchi tokenlari bloklanadi  
  _Invalidated tokens are blacklisted for security_

---

### ⚙️ Developerlar uchun (For Developers):
- 🛠 DRF API – barcha foydalanuvchi va profil funksiyalarini REST API orqali ishlatish mumkin  
  _Full-featured REST API for users and profiles_
- 📖 Swagger & Redoc dokumentatsiya – API hujjatlari avtomatik generatsiya qilinadi (`drf-spectacular` orqali)  
  _Auto-generated API docs with Swagger & Redoc_
- 🔍 Custom validation – faqat `@gmail.com` email orqali ro‘yxatdan o‘tish imkoniyati  
  _Custom email validation (only `@gmail.com` allowed)_
- 🧩 Extensible architecture – yangi app qo‘shishga tayyor modular tuzilma  
  _Modular architecture ready for new apps_

---

### 🎯 Qo‘shimcha imkoniyatlar (Additional Features):
- 🧾 Django Extensions – qo‘shimcha developer qulayliklari  
  _Extra tools for developers (via Django Extensions)_
- 🛡 Email-based account activation – foydalanuvchi faqat tasdiqlangandan keyin aktiv  
  _Account activation via email confirmation_
- 🌍 Kelajakda kengaytirish imkoniyati – yangi app (masalan, `tasks`, `core`, va boshqalar) qo‘shish mumkin  
  _Future-ready design to easily add new apps (e.g. `tasks`, `core`)_

---

## ⚙️ O‘rnatish bo‘yicha qo‘llanma (Installation Guide)

### 1️⃣ Repozitoriyani yuklab oling (Clone the repository):
```bash
git clone https://github.com/aabdurakhmanov/bajarvol.git
cd bajarvol
```

2️⃣ Virtual muhit yarating va faollashtiring (Create and activate virtual environment):
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3️⃣ Kerakli kutubxonalarni o‘rnating (Install dependencies):
```bash
pip install -r requirements.txt
```

4️⃣ Ma’lumotlar bazasini sozlang (Setup database):
```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Superuser yarating (Create superuser):
```bash
python manage.py createsuperuser
```

6️⃣ Serverni ishga tushiring (Run the server):
```bash
python manage.py runserver
```

📖 API Hujjatlari (API Documentation)
```bash
Swagger UI: http://127.0.0.1:8000/api/schema/
Redoc UI: http://127.0.0.1:8000/api/docs/
Redoc UI: http://127.0.0.1:8000/api/redoc/
```

🔮 Kelajak rejalari (Future Plans)
📌 Task management app qo‘shish
📌 Payment integration (Stripe/PayPal)
📌 Frontend (Vue.js/React) bilan integratsiya
📌 Multi-language support (Uzbek, English, German)


## 📸 Ekran rasmlari (Screenshots)
https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png
### 📝 Ro‘yxatdan o‘tish (Register)
![Register](https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png
)
https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png
### 🔑 Login
![Login](<img width="1366" height="683" alt="login" src="https://github.com/user-attachments/assets/50abd561-4091-40c0-8fdc-590e72a716bd" />
)
https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png
### 👤 Profil
![Profile](<img width="1365" height="675" alt="design" src="https://github.com/user-attachments/assets/dab69967-4235-4682-91f6-73210aaeb9ef" />
)
https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png

### 👤 Profil-me
![Profile](<img width="1365" height="678" alt="user-profile-bingo-djangoadminpanel png" src="https://github.com/user-attachments/assets/4b4ff00f-bb21-4823-aea4-2be8d3de3817" />
)
https://user-images.githubusercontent.com/76531073/178923741-80e6723f-2454-430f-8431-f299da22ff08.png

[![Django Rest Framework](https://img.shields.io/badge/DRF-Django%20Rest%20Framework-red?style=flat&logo=django)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-green?style=flat&logo=jsonwebtokens)](https://jwt.io/)
[![Google reCAPTCHA](https://img.shields.io/badge/Security-reCAPTCHA-blue?style=flat&logo=google)](https://www.google.com/recaptcha/about/)
[![Django Extensions](https://img.shields.io/badge/Tools-Django%20Extensions-orange?style=flat&logo=python)](https://django-extensions.readthedocs.io/)
[![drf-spectacular](https://img.shields.io/badge/API-DRF%20Spectacular-purple?style=flat&logo=swagger)](https://drf-spectacular.readthedocs.io/)







