# Generated by Django 3.2.13 on 2024-03-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_enquiry_table_dropdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry_table',
            name='dropdown',
            field=models.CharField(default=None, max_length=100),
        ),
    ]