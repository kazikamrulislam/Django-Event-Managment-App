# Generated by Django 5.1.2 on 2024-11-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_rename_content_event_event_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='evennt_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]