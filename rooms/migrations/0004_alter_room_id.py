# Generated by Django 3.2.12 on 2023-12-12 07:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_meetingroom_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
