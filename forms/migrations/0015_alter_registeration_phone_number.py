# Generated by Django 4.0.6 on 2022-07-14 04:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0014_alter_registeration_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='NATIONAL', max_length=128, region=None, unique=True),
        ),
    ]