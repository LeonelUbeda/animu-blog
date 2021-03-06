# Generated by Django 3.0.8 on 2020-07-29 07:14

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200728_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medialink',
            name='codec',
        ),
        migrations.RemoveField(
            model_name='medialink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='medialink',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='medialink',
            name='subs',
        ),
        migrations.RemoveField(
            model_name='medialink',
            name='title',
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('codec', models.CharField(choices=[('X265', 'x265'), ('X264', 'x264')], default='X264', max_length=5)),
                ('resolution', models.CharField(choices=[('480', '480p'), ('720', '720p'), ('1080', '1080p'), ('Another', 'Otro...')], default='1080', max_length=10)),
                ('subs', models.CharField(choices=[('SOFT', 'Softsubs'), ('HARD', 'Hardsubs')], default='HARD', max_length=10)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_types', to='posts.BasePost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='medialink',
            name='media_type',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='posts.MediaType'),
        ),
    ]
