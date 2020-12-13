# Generated by Django 3.0.8 on 2020-07-30 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('posts', '0008_auto_20200729_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animepost',
            name='download',
        ),
        migrations.AddField(
            model_name='animepost',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='medialink',
            name='server',
            field=models.CharField(choices=[('MG', 'Mega'), ('DP', 'Dropbox'), ('GD', 'Google Drive'), ('TG', 'Telegram')], default='GD', help_text='holas', max_length=2),
        ),
    ]