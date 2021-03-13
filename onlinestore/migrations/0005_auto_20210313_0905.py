# Generated by Django 3.1.7 on 2021-03-13 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0004_product_pricce'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='onlinestore.category'),
        ),
    ]
