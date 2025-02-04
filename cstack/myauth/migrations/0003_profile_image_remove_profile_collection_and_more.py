# Generated by Django 4.0 on 2024-05-17 08:45

from django.db import migrations, models
import myauth.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
        ('myauth', '0002_remove_cstackuser_entry_era_cstackuser_collection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/user_images/', validators=[myauth.validators.validate_image_size]),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='collection',
        ),
        migrations.AddField(
            model_name='profile',
            name='collection',
            field=models.ManyToManyField(blank=True, to='cards.Card'),
        ),
    ]
