# Generated by Django 5.1.1 on 2024-09-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='notes',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
