# Generated by Django 3.0.8 on 2020-07-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200718_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeEpisode',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.BasePost')),
            ],
            options={
                'abstract': False,
            },
            bases=('posts.basepost',),
        ),
    ]