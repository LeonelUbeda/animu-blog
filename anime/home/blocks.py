from wagtail.core import blocks
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _
class MenuSubItem(blocks.StructBlock):
    title = blocks.CharBlock(max_length=30, required=True)
    page = blocks.PageChooserBlock(
        required=False,
        label="Pagina",
        help_text="Si selecciona una pagina, se usará antes que la URL",
    )
    url = blocks.URLBlock(
        required=False,
        label="Pagina",
        help_text="Url custom",
    )
    def clean(self, value):
        errors = {}

        if not value.get('url') and value.get('page') is None:
            errors['url'] = ErrorList(['You must select a page, or enter a URL. Please fill just one of these fields.'])
            errors['page'] = ErrorList(['You must select a page, or enter a URL. Please fill just one of these fields.'])
        if errors:
            raise ValidationError('Validation error in StructBlock', params=errors)

        return super().clean(value)
class MenuItem(blocks.StructBlock):
    title = blocks.CharBlock(max_length=30, required=True)
    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)
    childs = blocks.ListBlock(MenuSubItem)
    
    def clean(self, value):
        return super().clean(value)