# Generated by Django 4.0.6 on 2022-08-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0013_rename_social_links_social_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='Registration_Closed',
            field=models.BooleanField(default=False),
        ),
    ]
