# Generated by Django 3.0.2 on 2020-02-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0002_auto_20200201_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='news', to='mynews.Tag'),
        ),
    ]
