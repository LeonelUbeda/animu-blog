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


