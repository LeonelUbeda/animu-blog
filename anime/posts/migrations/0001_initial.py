# Generated by Django 3.0.8 on 2020-07-13 22:07

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnimePost',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([], blank=True, null=True)),
                ('download', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('server', wagtail.core.blocks.ChoiceBlock(choices=[('MG', 'Mega.zn'), ('MF', 'Mediafire'), ('DB', 'Dropbox')], help_text='Servidor')), ('links', wagtail.core.blocks.CharBlock(help_text='Enlace de descarga', max_length=100, required=True))]))])),
                ('cover_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('genres', modelcluster.fields.ParentalManyToManyField(blank=True, to='posts.Genre')),
                ('tags', modelcluster.fields.ParentalManyToManyField(blank=True, to='posts.Tag')),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Animes',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AliasAnimePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='posts.AnimePost')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
