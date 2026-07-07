# NewsWave – Django News Website

A fully-featured news website built with Django, inspired by the Xapify template design,
powered by [NewsAPI](https://newsapi.org/).

---

## Project Structure

```
newssite/
├── manage.py
├── requirements.txt
├── newssite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── news/
    ├── views.py          ← All page logic + NewsAPI calls
    ├── urls.py           ← 6 URL routes
    ├── static/news/
    │   ├── css/style.css
    │   └── js/main.js
    └── templates/news/
        ├── base.html     ← Navbar, footer, ticker
        ├── home.html     ← Hero + category rows
        ├── category.html ← Category listing
        ├── search.html   ← Search results
        ├── detail.html   ← Article detail + sidebar
        ├── about.html
        ├── contact.html
        └── partials/
            └── card.html ← Reusable article card
```

## URL Routes

| URL | View | Page |
|-----|------|------|
| `/` | `home` | Homepage with hero & category rows |
| `/category/<cat>/` | `category` | Category articles (general/tech/sports/…) |
| `/search/` | `search` | Keyword search results |
| `/article/` | `article_detail` | Article detail page |
| `/about/` | `about` | About page |
| `/contact/` | `contact` | Contact form |

---

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your NewsAPI key
Open `newssite/settings.py` and replace:
```python
NEWS_API_KEY = 'YOUR_NEWS_API_KEY_HERE'
```
Get a free key at https://newsapi.org/register

### 3. Run migrations (for admin)
```bash
python manage.py migrate
```

### 4. Start the development server
```bash
python manage.py runserver
```

### 5. Open your browser
Visit http://127.0.0.1:8000/

---

## Features

- **Live news** from NewsAPI across 7 categories
- **Breaking news ticker** auto-scrolling headlines
- **Mega dropdown** navigation menu
- **Hero/featured** section with big + small cards
- **Article detail** page with social sharing buttons
- **Search** across all sources using keyword
- **Responsive** mobile-friendly design
- **Sticky header** + mobile hamburger menu
- Inspired by the **Xapify** news/blog template design

---

## Customization

- Colors: Edit CSS variables in `static/news/css/style.css` (look for `#007BFF`)
- Site name: Change "NewsWave" in `base.html`
- Categories: Edit the `CATEGORIES` list in `news/views.py`
- API region: Change `country='us'` in views to any 2-letter country code
