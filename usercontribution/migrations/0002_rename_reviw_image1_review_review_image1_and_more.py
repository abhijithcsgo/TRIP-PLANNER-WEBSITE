# Generated by Django 4.2.6 on 2024-02-17 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usercontribution', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviw_image1',
            new_name='review_image1',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='reviw_image2',
            new_name='review_image2',
        ),
        migrations.CreateModel(
            name='Newspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotname', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('descrption', models.CharField(max_length=250)),
                ('new_spot_image1', models.ImageField(blank=True, default=None, null=True, upload_to='new_spot_images/')),
                ('new_spot_image2', models.ImageField(blank=True, default=None, null=True, upload_to='new_spot_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]