# Generated by Django 4.1.5 on 2023-01-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_new_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
