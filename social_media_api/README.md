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






# Social Media API

Django REST API for managing posts and comments with authentication, pagination, and search.

---

## Setup

1. Clone repo & install dependencies:
   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
API base URL: http://localhost:8000/api/

Docs:

Swagger: /swagger/

ReDoc: /redoc/

Authentication
Use token auth for write operations:

makefile
Copy code
Authorization: Token your_token
Endpoints
Posts
Method	Endpoint	Auth	Description
GET	/api/posts/	No	List posts (paginated)
POST	/api/posts/	Yes	Create post
GET	/api/posts/{id}/	No	Retrieve post
PUT	/api/posts/{id}/	Yes	Update post (author only)
DELETE	/api/posts/{id}/	Yes	Delete post (author only)

Create Post Example:

json
Copy code
{
  "title": "My Post",
  "content": "Content here"
}
Comments
Method	Endpoint	Auth	Description
GET	/api/comments/	No	List comments (paginated)
POST	/api/comments/	Yes	Create comment
GET	/api/comments/{id}/	No	Retrieve comment
PUT	/api/comments/{id}/	Yes	Update comment (author only)
DELETE	/api/comments/{id}/	Yes	Delete comment (author only)

Create Comment Example:

json
Copy code
{
  "post": 1,
  "content": "Nice post!"
}
Features
Pagination: 10 items/page (?page=2)

Search posts by title or content: ?search=keyword

Permissions: users can only modify their own posts/comments

Errors
400: Bad request

401: Unauthorized

403: Forbidden

404: Not found

Example:

json
Copy code
{"detail": "You do not have permission to perform this action."}
