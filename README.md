# Collab

Collab is a Django-based project/idea-sharing platform where users create posts under topics, discuss them in threaded comments, and search across topics, post titles, and descriptions — a minimal Reddit-style forum for collaborating on projects.

## Features

- **User accounts** — register, log in, and log out (Django's built-in auth system)
- **Topics** — posts are organized under topics; the home page lists all topics for browsing
- **Posts** — authenticated users can create, edit, and delete their own posts (title, description, topic, host)
- **Messages/Comments** — any signed-in user can leave a message on a post's detail page, listed newest first
- **Search** — the home page search box filters posts by topic name, post name, or description
- **Access control** — only a post's host can edit or delete it

## Tech Stack

- [Python](https://www.python.org/) 3
- [Django](https://www.djangoproject.com/) 4.0.4
- SQLite (default development database)
- Django Templates + Bootstrap-style CSS for the frontend

## Project Structure

```
collab/
├── collab/             # Project configuration (settings, root URLs, WSGI/ASGI)
├── base/                # Main application
│   ├── models.py         # Topic, Post, Message models
│   ├── views.py           # Auth, home, post CRUD, and messaging views
│   ├── forms.py            # PostForm (ModelForm)
│   ├── urls.py              # App-level routes
│   ├── admin.py              # Django admin registrations
│   └── templates/base/        # App-specific templates (home, posts, forms, auth)
├── templates/            # Shared templates (base layout, navbar)
├── manage.py              # Django management entry point
└── db.sqlite3               # Development database
```

## Data Model

- **Topic** — `name`
- **Post** — `host` (User), `topic` (Topic), `name`, `description`, `created`, `updated`
- **Message** — `user` (User), `post` (Post), `body`, `created`, `updated`

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository and move into the project directory:
   ```bash
   git clone <repository-url>
   cd collab
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. (Optional) Create an admin/superuser account:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. The Django admin is available at `/admin/`.

## Usage

- Register a new account or log in from the navbar.
- Use **Create Post** on the home page to add a new post under a topic.
- Click a post to view it and post messages in its discussion thread.
- Use the search bar in the navbar to filter posts by topic, name, or description.
- Post hosts can edit or delete their own posts from the home page.

## Routes

| Path | View | Description |
|---|---|---|
| `/` | `home` | List/search posts and topics |
| `/posts/<id>` | `posts` | View a post and its messages; post a new message |
| `/create-post/` | `createPost` | Create a new post (login required) |
| `/update-post/<id>` | `updatePost` | Edit a post you host (login required) |
| `/delete-post/<id>` | `deletePost` | Delete a post you host (login required) |
| `/login/` | `loginPage` | Log in |
| `/register/` | `registerPage` | Register a new account |
| `/logout/` | `logoutUser` | Log out |
| `/admin/` | Django admin | Site administration |

## Notes

- `DEBUG = True` and the `SECRET_KEY` in [collab/settings.py](collab/settings.py) are development defaults — do not use them as-is in production.
- The bundled `db.sqlite3` is a development database and not meant for production use.
