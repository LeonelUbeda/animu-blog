from django import template
register = template.Library()
from ..models import MediaLink



@register.inclusion_tag('partials/posts/_links.html', takes_context=True)
def links_posts(context):
    servers_images = {
        MediaLink.MEGA: 'mega.png',
        MediaLink.GOOGLE_DRIVE: 'gugoldrive.png'
    }
    subs_text = {
        MediaLink.HARD_SUBS: 'Hardsubs',
        MediaLink.SOFT_SUBS: 'Softsubs'
    }

    links = []
    for link in context['page'].links.all():
        # import pdb; pdb.set_trace()
        links.append({
            'icon': servers_images[link.server],
            'subs': subs_text[link.subs]
        })
    context['links'] = links
    return context