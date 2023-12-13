# Generated by Django 4.2.4 on 2023-10-25 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dominus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='owner',
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_organization', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='owned_organizations', to=settings.AUTH_USER_MODEL),
        ),
    ]