from django.db import models
from django import forms
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

# TAGS
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


from wagtail.core import blocks
from wagtail.core.models import Page, Orderable, PageBase
from wagtail.core.fields import RichTextField, StreamField

#PANELS
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
#SNIPPETS
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

#BLOCKS
from .blocks import LinkBlock, RichTextBlock, LinkToParentBlock


#por ejemplo tags 1080p 720p DropBox Mega
class MediaTag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.name

register_snippet(MediaTag)


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        ImageChooserPanel("cover_image")
    ]
    def __str__(self):
        return self.name

register_snippet(Genre)

class Author(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )


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


class BasePostTag(TaggedItemBase):
    content_object = ParentalKey(
        'posts.BasePost',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )



class BasePost(Page):
    parent_page_types = ['home.AnimeHome']
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    tags = ClusterTaggableManager(through=BasePostTag, blank=True)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    excerpt = models.CharField(max_length=80, null=True, blank=False)
    content = StreamField([
        ("richtext_block", RichTextBlock()),
        ("link_to_parent_block", LinkToParentBlock())
    ], blank=True, null=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel("cover_image"),
        StreamFieldPanel("content"),
        FieldPanel("excerpt"),
        FieldPanel("tags")
    ]

class AnimePost(BasePost):
    template = 'posts/anime_post.html'

    download = StreamField([
        ("link", LinkBlock())
    ])

    genres = ParentalManyToManyField("posts.Genre", blank=True, related_name="genres")
    mediatag = ParentalManyToManyField("posts.MediaTag", blank=True, related_name="mediatag")
    content_panels = BasePost.content_panels + [
        MultiFieldPanel([
            InlinePanel("aliases")
        ], "Alias"),

        MultiFieldPanel([
            FieldPanel("genres", widget=forms.CheckboxSelectMultiple),
            FieldPanel("mediatag", widget=forms.CheckboxSelectMultiple),
        ], "Clasificaciones"),
    ]

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"

class AnimeEpisode(BasePost):
    template = 'posts/anime_episode.html'
    parent_page_types = ['posts.AnimePost']