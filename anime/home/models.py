from django.db import models

from wagtail.core.models import Page

from posts.models import AnimePost

class HomePage(Page):
    max_count = 1
    pass

class TopMenu(models.Model):
    pass

class AnimeHome(Page):
    template = 'home/anime_home.html'




    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["featured"] = self.get_children().live().public().specific()[:3]
        # import pdb; pdb.set_trace()
        context['lastest_anime'] = self.get_children().live().public().specific()[:10]
        return context

    max_count = 1