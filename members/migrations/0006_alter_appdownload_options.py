# Generated by Django 4.1 on 2023-11-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_appdownload_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appdownload',
            options={'verbose_name': 'App Download', 'verbose_name_plural': 'app Downloads'},
        ),
    ]