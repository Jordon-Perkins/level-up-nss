# Generated by Django 4.1.6 on 2023-02-21 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attendees', through='levelupapi.GamerEvent', to='levelupapi.gamer'),
        ),
        migrations.AlterField(
            model_name='gamerevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_gamer', to='levelupapi.event'),
        ),
        migrations.AlterField(
            model_name='gamerevent',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamer_event', to='levelupapi.gamer'),
        ),
    ]
