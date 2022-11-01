# Generated by Django 3.2 on 2022-10-31 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.columns')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.columns')),
            ],
        ),
        migrations.CreateModel(
            name='Store_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.store')),
            ],
        ),
        migrations.CreateModel(
            name='store_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.orders')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.store')),
            ],
        ),
    ]