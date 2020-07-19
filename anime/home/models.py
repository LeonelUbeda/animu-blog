from django.db import models

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from posts.models import AnimePost
from wagtail.core.models import Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, PageChooserPanel
from wagtail.core import blocks
from .blocks import MenuItem

class HomePage(Page):
    max_count = 1
    pass

class TopMenu(models.Model):
    pass

@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=30, blank=False, null=True)
    panels = [
        FieldPanel("title"),
        InlinePanel("items", label="add items")
    ]

class MenuItems(Orderable, ClusterableModel):
    title = models.CharField(max_length=30, blank=False, null=True)
    page = ParentalKey("home.Menu", related_name="items")
    url = models.URLField(blank=True, null=True)
    page_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
        PageChooserPanel("page_link"),
        InlinePanel("subitems", label="add sub items")
    ]


class SubItemMenu(Orderable):
    title = models.CharField(max_length=30, blank=False, null=True)
    page = ParentalKey("home.MenuItems", related_name="subitems")
    url = models.URLField(blank=True, null=True)
    page_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
        PageChooserPanel("page_link"),
    ]


class AnimeHome(Page):

    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)

    template = 'home/anime_home.html'
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["featured"] = self.get_children().live().public().specific()[:3]
        context['lastest_anime'] = self.get_children().live().public().specific()[:10]
        return context

    content_panels = Page.content_panels + [
        FieldPanel("menu")
    ]
    max_count = 1


# class FeaturedHomePage(Page):