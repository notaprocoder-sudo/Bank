# Generated by Django 4.1.4 on 2023-03-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust',
            name='Cheque_book',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cust',
            name='Credit_Card',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cust',
            name='Debit_Card',
            field=models.CharField(max_length=20),
        ),
    ]