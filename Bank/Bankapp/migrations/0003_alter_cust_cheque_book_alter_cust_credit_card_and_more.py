# Generated by Django 4.1.4 on 2023-03-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0002_alter_cust_cheque_book_alter_cust_credit_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust',
            name='Cheque_book',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cust',
            name='Credit_Card',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cust',
            name='Debit_Card',
            field=models.CharField(max_length=50),
        ),
    ]
