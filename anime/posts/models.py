from django.db import models
from django import forms
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
#PANELS
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
#SNIPPETS
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

#BLOCKS
from .blocks import LinkBlock


#por ejemplo tags 1080p 720p DropBox Mega
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.name

register_snippet(Tag)


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
register_snippet(Genre)

# class TagsAnimePost(Orderable):
#     page = ParentalKey("posts.AnimePost", related_name="tags")
#     tag = models.ForeignKey("posts.Tags", on_delete=models.CASCADE)
#     panels = [
#         SnippetChooserPanel("tag")
#     ]

# class GenreAnimePost(Orderable):
#     page = ParentalKey("posts.AnimePost", related_name="genre")
#     genre = models.ForeignKey("posts.Genre", on_delete=models.CASCADE)
#     panels = [
#         SnippetChooserPanel("genre")
#     ]

class AliasAnimePost(Orderable):
    page = ParentalKey("posts.AnimePost", related_name="aliases")
    name = models.CharField(max_length=100, blank=False, null=False)
    panels = [
        FieldPanel("name")
    ]


# class Author(models.Model):
#     name = models.CharField(max_length=50, blank=False, null=False)




class AnimePost(Page):
    template = 'posts/anime_post.html'

    parent_page_types = ['home.AnimeHome']
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    excerpt = models.CharField(max_length=80, null=True, blank=False)
    content = StreamField([], blank=True, null=True)

    download = StreamField([
        ("link", LinkBlock())
    ])

    genres = ParentalManyToManyField("posts.Genre", blank=True, related_name="genres")
    tags = ParentalManyToManyField("posts.Tag", blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("cover_image"),
        StreamFieldPanel("content"),
        FieldPanel("excerpt"),
        MultiFieldPanel([
            InlinePanel("aliases")
        ], "Alias"),

        MultiFieldPanel([
            FieldPanel("genres", widget=forms.CheckboxSelectMultiple),
            FieldPanel("tags", widget=forms.CheckboxSelectMultiple)
        ], "Clasificaciones"),
    ]

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"