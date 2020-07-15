from django.db import models

from wagtail.core.models import Page
from posts.models import Tag, Genre
from posts.models import AnimePost
from random import randint
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
        context['tags'] = Tag.objects.all()
        context['genres'] = Genre.objects.all()
        
        children_quantity = self.get_children_count()
        random_index = randint(0, children_quantity - 1)
        
        context['random'] = self.get_children().live().public().specific()[random_index]

        context['lastest_anime'] = self.get_children().live().public().specific()[:10]
        return context

    max_count = 1