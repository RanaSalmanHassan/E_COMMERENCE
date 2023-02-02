# Generated by Django 4.1.1 on 2022-12-26 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('name', models.CharField(max_length=100)),
                ('prieview_text', models.CharField(max_length=200, verbose_name='Priview Text')),
                ('details_text', models.CharField(max_length=500, verbose_name='Description')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(default=0.0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shop.category')),
            ],
        ),
    ]
