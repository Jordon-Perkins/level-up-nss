# Generated by Django 4.1.6 on 2023-02-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_event_attendees_alter_gamerevent_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='events_attending', through='levelupapi.GamerEvent', to='levelupapi.gamer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_organizing', to='levelupapi.gamer'),
        ),
    ]