# Generated by Django 4.2.2 on 2023-06-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='stripe_payment_intent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
