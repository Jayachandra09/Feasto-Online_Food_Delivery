#  🛵 Feast - Food Delivery App 

A Django-based backend project for a food delivery application. This project focuses on backend functionality like vendor registration, dynamic cart operations, location autocomplete, and more.

## 📌 Features

- **Vendor Registration & Authentication**
  - Custom user model with role-based access (Vendor, Customer)
  - Email verification using Django’s SMTP backend

- **Google Maps API Integration**
  - Autocomplete location search
  - Fetches and stores complete location metadata (latitude, longitude, pincode, etc.)

- **Cart Functionality (AJAX-powered)**
  - Add/Delete items dynamically without refreshing the page
  - Auto-update cart totals and quantity on user interaction

- **Vendor & Menu Management**
  - Vendors can create/update food items and manage menu listings

- **PostgreSQL Integration**
  - Switched from default SQLite to PostgreSQL for production-readiness

- **Form Handling & Model Relationships**
  - Robust form validation using Django Forms
  - Models connected with OneToOneField, ForeignKey, and ManyToManyField

## 🏗️ Tech Stack

- Python 3.10
- Django 4.x
- PostgreSQL
- Google Maps Platform API
- AJAX (for cart updates)
- Hosted in local virtual environment (venv)

## 🚀 Getting Started

1. Clone the repository

```bash
git clone https://github.com/Jayachandra09/Feasto-Online_Food_Delivery.git
cd food-delivery-app
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables and `settings.py` (e.g., email, Google API keys)

5. Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

## 📂 Project Structure

```
food-delivery-app/
├── accounts/
├── marketplace/
├── templates/
├── static/
├── media/
├── manage.py
└── README.md
```

## 🧪 Sample Data

To populate with sample restaurants and items, you can use Django Admin or create fixtures.

## 🛠️ Note

If you do not have a `requirements.txt`, you can generate one using:

```bash
pip freeze > requirements.txt
```

## 📄 License

This project is for educational purposes.

---

Made with ❤️ by [Jayachandra]