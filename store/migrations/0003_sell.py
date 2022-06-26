# Generated by Django 4.0.5 on 2022-07-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('contactnumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('itemimage', models.FileField(default='default.jpg', upload_to='static/images/items')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
