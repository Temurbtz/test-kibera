# Generated by Django 4.1.5 on 2023-01-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_news_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
