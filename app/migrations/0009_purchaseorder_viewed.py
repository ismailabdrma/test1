# Generated by Django 4.2.1 on 2023-09-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_purchaseorder_confirmed_purchaseorder_not_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]