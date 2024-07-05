# Generated by Django 4.0.4 on 2024-07-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bimage', models.URLField()),
            ],
        ),
    ]