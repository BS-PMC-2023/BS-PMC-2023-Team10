# Generated by Django 4.1.7 on 2023-05-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_alter_order_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamageReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
