## API Endpoints for Books

| Method | Endpoint              | Description                | Permission            |
|--------|-----------------------|----------------------------|------------------------|
| GET    | /api/books/           | List all books             | Public                |
| GET    | /api/books/<id>/      | Retrieve a specific book   | Public                |
| POST   | /api/books/create/    | Create a new book          | Authenticated users   |
| PUT    | /api/books/<id>/update/ | Update a book            | Authenticated users   |
| DELETE | /api/books/<id>/delete/ | Delete a book            | Authenticated users   |

## Notes
- The `BookSerializer` handles validation (e.g., title length).
- Authenticated users must provide a valid token using headers like:
  `Authorization: Token <your_token>`


  ##  Book API - Query Parameters

###  Filtering
- `/api/books/?author=George Orwell`
- `/api/books/?publication_year=2023`

###  Searching
- `/api/books/?search=1984`
- `/api/books/?search=Orwell`

###  Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`

###  Combined Example
- `/api/books/?author=Orwell&search=1984&ordering=-publication_year`
