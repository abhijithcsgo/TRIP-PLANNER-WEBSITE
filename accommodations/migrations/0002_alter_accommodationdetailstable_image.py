# Generated by Django 4.2.6 on 2024-01-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationdetailstable',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='accommodation_images/'),
        ),
    ]
