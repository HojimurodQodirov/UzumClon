# Generated by Django 5.0.7 on 2024-08-06 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstalledApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appstore_url', models.URLField()),
                ('playmarket_url', models.URLField()),
            ],
        ),
    ]
