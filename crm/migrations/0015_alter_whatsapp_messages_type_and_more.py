# Generated by Django 4.1 on 2023-11-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_whatsapp_messages_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
    ]