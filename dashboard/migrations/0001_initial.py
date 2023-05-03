# Generated by Django 4.1.7 on 2023-04-09 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('Serial Number', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics')], max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('Days To Loan', models.CharField(choices=[('1-2 Days', '1-2 Days'), ('3 Days - 1 Week', '3 Days - 1 Week'), ('1 Week - 2 Weeks', '1 Week - 2 Weeks'), ('Other', 'Other')], default='1-2 Days', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
