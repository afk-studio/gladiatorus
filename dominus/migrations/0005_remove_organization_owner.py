# Generated by Django 4.2.4 on 2023-10-25 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominus', '0004_organization_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='owner',
        ),
    ]