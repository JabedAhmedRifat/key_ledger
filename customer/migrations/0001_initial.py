# Generated by Django 4.2.3 on 2023-09-02 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_shop_name', models.CharField(max_length=255)),
                ('customer_shop_address', models.TextField()),
                ('contact_person_name', models.CharField(max_length=255)),
                ('contact_person_phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DebitCreditCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_balance', models.IntegerField(default=0)),
                ('credit_balance', models.IntegerField(default=0)),
                ('total_balance', models.IntegerField(default=0)),
                ('details', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]