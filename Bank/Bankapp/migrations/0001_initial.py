# Generated by Django 4.1.4 on 2023-03-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Date_of_Birth', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('Phone_Number', models.IntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('Account_type', models.CharField(choices=[('save', 'Savings Account'), ('current', 'Current Account'), ('def', 'Select')], default='def', max_length=20)),
                ('Cheque_book', models.BooleanField()),
                ('Debit_Card', models.BooleanField()),
                ('Credit_Card', models.BooleanField()),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bankapp.bran')),
                ('District', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bankapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='bran',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bankapp.district'),
        ),
    ]