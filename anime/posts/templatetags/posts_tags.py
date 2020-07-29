from django import template
register = template.Library()
from ..models import MediaLink, MediaType



@register.inclusion_tag('partials/posts/_links.html', takes_context=True)
def links_posts(context):
    servers_images = {
        MediaLink.MEGA: 'mega.png',
        MediaLink.GOOGLE_DRIVE: 'gugoldrive.png'
    }
    subs_text = {
        MediaType.HARD_SUBS: 'Hardsubs',
        MediaType.SOFT_SUBS: 'Softsubs'
    }
    resolution_text = {
        MediaType.RES_1080: '1080p',
        MediaType.RES_720: '1080p',
        MediaType.RES_480: '480p'
    }
    codec_text = {
        MediaType.X264: 'x264',
        MediaType.X265: 'x265'
    }
    media_types = []
    for media in context['page'].media_types.all():
        media_types.append({
            'codec': codec_text[media.codec],
            'resolution': resolution_text[media.resolution],
            'subtitles': subs_text[media.subs],
            'links': [{
                'icon': servers_images[i.server],
                'link': i.link
            } for i in media.links.all()]
        })
        # import pdb; pdb.set_trace()
    context['media_types'] = media_types
    return context