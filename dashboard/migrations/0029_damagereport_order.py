# Generated by Django 4.1.7 on 2023-05-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_order_is_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='damagereport',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.order'),
        ),
    ]
