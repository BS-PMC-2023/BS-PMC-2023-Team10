# Generated by Django 4.1.7 on 2023-04-09 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Days To Loan',
        ),
    ]
