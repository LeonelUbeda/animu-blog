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
from .blocks import LinkBlock, RichTextBlock, LinkToParentBlock, MediaLink


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

class MediaLink(Orderable):
    MEGA = 'MG'
    DROPBOX = 'DP'
    GOOGLE_DRIVE = 'GD'
    TELEGRAM = 'TG'
    SERVERS_CHOICES = [
        (MEGA, 'Mega'),
        (DROPBOX, 'Dropbox'),
        (GOOGLE_DRIVE, 'Google Drive'),
        (TELEGRAM, 'Telegram'),
    ]
    server = models.CharField(max_length=2, choices=SERVERS_CHOICES, default=GOOGLE_DRIVE, help_text="holas")
    link = models.CharField(max_length=80, null=True, blank=False)
    media_type = ParentalKey("posts.Mediatype", related_name="links", null=True)

class MediaType(ClusterableModel, Orderable):

    title = models.CharField(max_length=100, null=True, blank=True)

    X265 = 'X265'
    X264 = 'X264'

    CODEC_CHOICES = [
        (X265, 'x265'),
        (X264, 'x264')
    ]
    codec = models.CharField(max_length=5, choices=CODEC_CHOICES, default=X264)

    RES_480 = '480'
    RES_720 = '720'
    RES_1080 = '1080'
    RES_ANOTHER = 'Another'

    RESOLUTION_CHOICES = [
        (RES_480, '480p'),
        (RES_720, '720p'),
        (RES_1080, '1080p'),
        (RES_ANOTHER, 'Otro...')
    ]
    resolution = models.CharField(max_length=10, choices=RESOLUTION_CHOICES, default=RES_1080)


    SOFT_SUBS = 'SOFT'
    HARD_SUBS = 'HARD'
    SUBS_CHOICES = [
        (SOFT_SUBS, 'Softsubs'),
        (HARD_SUBS, 'Hardsubs')
    ]
    subs = models.CharField(max_length=10, choices=SUBS_CHOICES, default=HARD_SUBS)
    page = ParentalKey("posts.BasePost", related_name="media_types")
    panels = [
        FieldPanel("codec"),
        FieldPanel("resolution"),
        FieldPanel("subs"),
        InlinePanel("links", label="Links")
    ]

class BasePost(Page):
    parent_page_types = ['home.AnimeHome']
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    is_creatable = False
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
            InlinePanel("media_types"),
        ], "Media types"),
        MultiFieldPanel([
            FieldPanel("genres", widget=forms.CheckboxSelectMultiple),
            FieldPanel("mediatag", widget=forms.CheckboxSelectMultiple),
        ], "Clasificaciones"),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['episodes'] = self.get_children().live().public().specific()
        return context
    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"

class AnimeEpisode(BasePost):
    template = 'posts/anime_episode.html'
    parent_page_types = ['posts.AnimePost']
    subpage_types = []
    content_panels = BasePost.content_panels + [
        MultiFieldPanel([
            InlinePanel("media_types"),
        ], "Links"),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["parent"] = self.get_parent()
        context['next'] = self.get_next_sibling()
        context['prev'] = self.get_prev_sibling()
        return context