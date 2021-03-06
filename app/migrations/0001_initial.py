# Generated by Django 2.1.7 on 2019-04-03 03:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('postal_code', models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(message="Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed.", regex='^[0-9]+$')])),
                ('office_address', models.CharField(max_length=100)),
                ('building_name', models.CharField(blank=True, max_length=100)),
                ('memo', models.TextField(blank=True, max_length=300)),
                ('card_img', models.FileField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CardClassification'),
        ),
    ]
