# Generated by Django 4.2.3 on 2023-07-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_options_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]