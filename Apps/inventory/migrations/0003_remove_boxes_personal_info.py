# Generated by Django 4.0.6 on 2023-04-12 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxes',
            name='personal_info',
        ),
    ]
