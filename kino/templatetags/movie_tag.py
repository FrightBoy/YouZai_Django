from django import template
from kino.models import Category, Movie

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('kino/tags/last_movie.html')
def get_last_movie(count=5):
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movie': movies}
