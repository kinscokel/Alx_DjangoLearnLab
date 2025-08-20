# Social Media API

A simple social media API built with Django and Django REST Framework.

## Features

- User registration
- Token-based login
- Profile viewing and editing
- Custom user model with bio, profile picture, and followers

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/social_media_api
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run server:
    ```
    python manage.py runserver
    ```

## API Endpoints

| Endpoint            | Method | Description           |
|---------------------|--------|-----------------------|
| `/api/accounts/register/` | POST   | Register a new user |
| `/api/accounts/login/`    | POST   | Login and get token |
| `/api/accounts/profile/`  | GET/PUT | Manage profile     |

