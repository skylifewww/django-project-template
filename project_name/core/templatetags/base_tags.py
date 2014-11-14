import re

from purl import URL

from django.utils.encoding import force_text

from django_jinja import library
lib = library.Library()


@library.filter
def intspace(value):
    """
    45570 => 45 570
    450840 => 450 840
    1450000 => 1 450 000
    """
    orig = force_text(value)
    new = re.sub(r'^(-?\d+)(\d{3})', '\g<1> \g<2>', orig)
    if orig == new:
        return new
    return intspace(new)


@lib.global_function
def set_param(request=None, url=None, **kwargs):
    """
    # http://localhost:8000/?q=test&page=3
    <a href="{{ set_param(request, page=4) }}">Page 4</a>
    Result:
    <a href="/?q=test&page=4">Страница 4</a>
    """
    if not request and not url:
        return '/'
    url = URL(path=request.path, query=request.META['QUERY_STRING']) if request else URL(url)
    for k, v in kwargs.iteritems():
        url = url.query_param(k, v)
    return url.as_string()
