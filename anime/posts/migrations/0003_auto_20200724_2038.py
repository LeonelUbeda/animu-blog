# Generated by Django 3.0.8 on 2020-07-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_animeepisode_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeepisode',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]