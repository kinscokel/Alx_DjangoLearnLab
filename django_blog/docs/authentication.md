# Authentication System – django_blog

## Overview
This document explains the user authentication system implemented in the `django_blog` project. It includes registration, login, logout, and user profile management functionalities.

---

## Features

- User Registration with username, email, and password
- User Login and Logout using Django’s built-in views
- User Profile Page with editable email
- CSRF protection and secure password handling

---

## URLs

| URL Path     | View            | Description                    |
|--------------|------------------|--------------------------------|
| `/register/` | `register_view`  | Register a new user            |
| `/login/`    | Django built-in  | Login user                     |
| `/logout/`   | Django built-in  | Logout user                    |
| `/profile/`  | `profile_view`   | View and update user email     |

---

## Setup Instructions

1. Ensure `'blog'` is in `INSTALLED_APPS`.
2. Templates are located in `blog/templates/registration/`.
3. Routes are defined in `blog/urls.py` or `django_blog/urls.py`.
4. Forms are defined in `blog/forms.py`.
5. Views are in `blog/views.py`.

---

## Testing Instructions

- Visit `/register/` and create a user.
- Login at `/login/`.
- Go to `/profile/` and update your email.
- Logout at `/logout/`.

---

## Security Notes

- All forms use `{% csrf_token %}` to prevent CSRF attacks.
- Passwords are stored securely using Django’s built-in hashing.
- Profile view is protected with `@login_required`.

---

## Additional Notes

- Templates use Django’s default structure under `registration/`.
- This approach does **not** use a separate app for users.
