import datetime
import time 
from django import template
from random import randint
from wagtail.core.models import Page
from home.models import AnimeHome
from posts.models import Tag, Genre, AnimePost
register = template.Library()

@register.inclusion_tag('partials/header.html', takes_context=True)
def header_blog(context):
    """ Get list of live blog pages that are descendants of this page """
    # page = context['page']
    # posts = BlogPost.objects.descendant_of(page).live().public().order_by('-date_published')[:4]

    page = context['page']
    #Esto lo hace multisitio sin problemas, no se para que, pero ahi ta

    #primero reviso si existe algun padre que sea tipo AnimeHome
    root = page.get_ancestors().type(AnimeHome).specific().last()

    #Si es none significa que entonces estamos en el main
    if root is None:
        #obtenemos la info del main
        root = AnimeHome.objects.get(pk=page.pk)
        
    # NOTE: No se que tan eficiente sera todo el proceso de arriba pero bueno...
    menu = getattr(root, "menu", None)
    print(menu)
    return {'menu': menu }


@register.inclusion_tag('partials/sidebar.html', takes_context=True)
def sidebar_blog(context):
    """ Get list of live blog pages that are descendants of this page """
    temp = {}

    # page = context['page']
    # posts = BlogPost.objects.descendant_of(page).live().public().order_by('-date_published')[:4]
    temp['tags'] = Tag.objects.all()
    temp['genres'] = Genre.objects.all()

    #Mejorar esto para que sea independiente por SITIO
    children_quantity = AnimePost.objects.all().count()
    random_index = randint(0, children_quantity - 1)

    import time
    start = time.process_time()
    temp['random'] = AnimePost.objects.all().live().public().specific()[random_index]
    print(time.process_time() - start)

    return temp