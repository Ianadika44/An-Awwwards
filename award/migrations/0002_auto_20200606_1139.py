# Generated by Django 3.0.7 on 2020-06-06 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name']},
        ),
    ]
