# Generated by Django 4.2 on 2023-04-19 13:14

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Salon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('phoneNumbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be in international format.', regex='^\\+?1?\\d{9,15}$')]), size=None)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffOfSalon', to='Salon.salon')),
            ],
        ),
    ]
