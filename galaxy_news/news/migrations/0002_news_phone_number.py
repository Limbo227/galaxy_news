# Generated by Django 4.0.1 on 2022-02-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='phone_number',
            field=models.CharField(default=1, max_length=100, verbose_name='phone_number'),
            preserve_default=False,
        ),
    ]