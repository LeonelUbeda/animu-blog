from wagtail.core import blocks

class MediaLink(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, required=False)
    media_type = blocks.ChoiceBlock(choices=[
        ('Mega', 'Mega'),
        ('gdrive', 'Google Drive'),
        ('telegram', 'Telegram'),
    ], required=True)
    link = blocks.CharBlock(max_length=200, required=True)
    from wagtail.core import blocks

class LinkBlock(blocks.StructBlock):
    MEGA = "MG"
    MEDIAFIRE = "MF"
    DROPBOX = "DB"
    server_choices = [
        ("MG", "Mega.zn"),
        ("MF", "Mediafire"),
        ("DB", "Dropbox")
    ]
    server = blocks.ChoiceBlock(choices=server_choices, help_text="Servidor", default=MEGA)
    links = blocks.CharBlock(max_length=100, help_text="Enlace de descarga", required=True)
    
    class Meta:
        template = "posts/download_block.html"


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = 'blocks/posts/richtext_block.html'
        icon = 'edit'
        label = 'Texto enriquecido'


class LinkToParentBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, required=True)
    class Meta:
        template = 'blocks/posts/link_to_parent_block.html'