import requests
from django.shortcuts import render

# ── GNews API config ──────────────────────────────────────────────────────────
API_KEY  = 'c11a684fb4b0bea5790bf3723cb8a1ee'
BASE_URL = 'https://gnews.io/api/v4/'

CATEGORIES = ['general', 'technology', 'business', 'sports', 'entertainment', 'health', 'science']

GNEWS_TOPICS = {
    'general':       'breaking-news',
    'technology':    'technology',
    'business':      'business',
    'sports':        'sports',
    'entertainment': 'entertainment',
    'health':        'health',
    'science':       'science',
}


def _fetch_topic(topic, max_articles=10):
    params = {
        'token': API_KEY,
        'topic': topic,
        'lang':  'en',
        'max':   max_articles,
    }
    try:
        r = requests.get(BASE_URL + 'top-headlines', params=params, timeout=8)
        data = r.json()
        return data.get('articles', [])
    except Exception:
        return []


def _fetch_search(q, max_articles=10):
    params = {
        'token':  API_KEY,
        'q':      q,
        'lang':   'en',
        'max':    max_articles,
        'sortby': 'publishedAt',
    }
    try:
        r = requests.get(BASE_URL + 'search', params=params, timeout=8)
        data = r.json()
        return data.get('articles', [])
    except Exception:
        return []


def _clean(articles):
    return [a for a in articles if a.get('title') and a.get('description')]


def _normalize(articles):
    """Map GNews fields to the same keys templates already use."""
    result = []
    for a in articles:
        result.append({
            'title':       a.get('title', ''),
            'description': a.get('description', ''),
            'content':     a.get('content', ''),
            'url':         a.get('url', ''),
            'urlToImage':  a.get('image', ''),
            'publishedAt': a.get('publishedAt', '')[:10],
            'author':      a.get('source', {}).get('name', ''),
            'source':      {'name': a.get('source', {}).get('name', '')},
        })
    return result


# ── Home ──────────────────────────────────────────────────────────────────────
def home(request):
    featured   = _normalize(_clean(_fetch_topic('breaking-news', max_articles=6)))
    technology = _normalize(_clean(_fetch_topic('technology',    max_articles=4)))
    business   = _normalize(_clean(_fetch_topic('business',      max_articles=4)))
    sports     = _normalize(_clean(_fetch_topic('sports',        max_articles=4)))

    ctx = {
        'featured':    featured,
        'technology':  technology,
        'business':    business,
        'sports':      sports,
        'categories':  CATEGORIES,
        'active_page': 'home',
    }
    return render(request, 'news/home.html', ctx)


# ── Category ──────────────────────────────────────────────────────────────────
def category(request, cat):
    topic    = GNEWS_TOPICS.get(cat, 'breaking-news')
    articles = _normalize(_clean(_fetch_topic(topic, max_articles=10)))
    ctx = {
        'articles':    articles,
        'category':    cat.title(),
        'categories':  CATEGORIES,
        'active_page': cat,
    }
    return render(request, 'news/category.html', ctx)


# ── Search ────────────────────────────────────────────────────────────────────
def search(request):
    query    = request.GET.get('q', '').strip()
    articles = []
    if query:
        articles = _normalize(_clean(_fetch_search(query, max_articles=10)))
    ctx = {
        'articles':   articles,
        'query':      query,
        'categories': CATEGORIES,
        'active_page': 'search',
    }
    return render(request, 'news/search.html', ctx)


# ── Article Detail ────────────────────────────────────────────────────────────
def article_detail(request):
    ctx = {
        'title':       request.GET.get('title', ''),
        'description': request.GET.get('description', ''),
        'content':     request.GET.get('content', ''),
        'url':         request.GET.get('url', ''),
        'urlToImage':  request.GET.get('image', ''),
        'source':      request.GET.get('source', ''),
        'publishedAt': request.GET.get('publishedAt', ''),
        'author':      request.GET.get('author', ''),
        'categories':  CATEGORIES,
        'active_page': '',
    }
    return render(request, 'news/detail.html', ctx)


# ── About ─────────────────────────────────────────────────────────────────────
def about(request):
    ctx = {'categories': CATEGORIES, 'active_page': 'about'}
    return render(request, 'news/about.html', ctx)


# ── Contact ───────────────────────────────────────────────────────────────────
def contact(request):
    sent = False
    if request.method == 'POST':
        sent = True
    ctx = {'categories': CATEGORIES, 'active_page': 'contact', 'sent': sent}
    return render(request, 'news/contact.html', ctx)
