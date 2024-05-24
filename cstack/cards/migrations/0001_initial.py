# Generated by Django 4.0 on 2024-04-24 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('release_year', models.IntegerField()),
                ('release_country', models.CharField(max_length=30)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('shop', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='card_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.cardcategory')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]