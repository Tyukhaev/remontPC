# Generated by Django 3.0.8 on 2020-09-10 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, verbose_name='Название услуги')),
                ('service_price', models.FloatField(verbose_name='Цена услуги')),
                ('service_description', models.TextField(verbose_name='Описание услуги')),
                ('service_averagetime', models.IntegerField(verbose_name='Среднее время')),
                ('service_images', models.ImageField(null=True, upload_to='')),
                ('service_mainservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainservices.MainService')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
