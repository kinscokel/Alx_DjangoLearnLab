

#  Django Blog - Blog Post Management

This is a simple Django blog project that supports **full CRUD operations** (Create, Read, Update, Delete) for blog posts using Django's **class-based views** (CBVs). Authenticated users can create, edit, and delete their own posts, while anyone can view published posts.

---

##  Features

-  View a list of all blog posts
-  View the details of a single blog post
-  Create new blog posts (authenticated users only)
-  Edit or delete blog posts (only the post's author)
-  Use of class-based views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
-  Secure access using Django's `LoginRequiredMixin` and `UserPassesTestMixin`
-  Clean, user-friendly templates for each view

---

##  URL Patterns

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/posts/` | `PostListView` | List all posts |
| `/posts/new/` | `PostCreateView` | Create a new post |
| `/posts/<int:pk>/` | `PostDetailView` | View a specific post |
| `/posts/<int:pk>/edit/` | `PostUpdateView` | Edit an existing post (author only) |
| `/posts/<int:pk>/delete/` | `PostDeleteView` | Delete a post (author only) |

---

##  Permissions & Access Control

-  **Create**: Only accessible by **authenticated** users.
-  **Update & Delete**: Only the **post's author** can edit or delete.
-  **List & Detail**: Publicly accessible to all users.

Implemented using:
- `LoginRequiredMixin` to restrict unauthenticated access
- `UserPassesTestMixin` to restrict actions to the post’s author

---

##  Forms

Blog posts are created and updated using a **ModelForm**:

- **Form Fields:** `title`, `content`
- The `author` is automatically assigned based on the logged-in user in the view.

Form is defined in: `blog/forms.py`

---

##  Templates

All templates are located in `templates/blog/`.

| Template | Purpose |
|----------|---------|
| `post_list.html` | Displays all blog posts |
| `post_detail.html` | Displays a single post's full content |
| `post_form.html` | Shared template for creating and editing posts |
| `post_confirm_delete.html` | Confirm deletion of a post |

All templates extend a base layout and include CSRF tokens for secure form submission.

---

##  Project Structure


In settings.py, ensure:


TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]
 Folder Structure

project/
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── logout.html

blog/
└── templates/
    └── blog/
        ├── post_list.html
        ├── post_detail.html
        └── comments/
            ├── add_comment.html
            ├── edit_comment.html
            └── delete_comment.html
 Comments Display (in post_detail.html)

{% for comment in post.comments.all %}
  <p><b>{{ comment.author }}</b>: {{ comment.content }}</p>
{% endfor %}

{% if user.is_authenticated %}
  <form method="post">{% csrf_token %}{{ form.as_p }}<button>Post</button></form>
{% else %}
  <a href="{% url 'login' %}?next={{ request.path }}">Log in to comment</a>
{% endif %}


# Tagging and Search Features

## Adding Tags
- When creating or editing a post, enter tags separated by commas.
- New tags are automatically created.

## Viewing Tags
- Tags appear under each post.
- Click on a tag to see all posts with that tag.

## Searching Posts
- Use the search bar in the header/footer to search by title, content, or tag name.
- Results will show posts matching your search query.