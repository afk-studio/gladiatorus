# Generated by Django 4.2.4 on 2023-10-20 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magistrate', '0003_remove_tournament_creator_and_more'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchseries',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='tournament.tournament'),
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
