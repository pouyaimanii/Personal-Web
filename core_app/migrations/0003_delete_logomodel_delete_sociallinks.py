# Generated by Django 5.2 on 2025-04-24 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_sociallinks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogoModel',
        ),
        migrations.DeleteModel(
            name='SocialLinks',
        ),
    ]
