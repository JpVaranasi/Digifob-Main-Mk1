# Generated by Django 5.0 on 2024-02-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearform',
            name='name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
