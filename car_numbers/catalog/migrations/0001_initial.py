# Generated by Django 5.1.1 on 2024-09-12 10:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6)),
                ('car', models.CharField(blank=True, max_length=60, null=True)),
                ('notes', models.TextField(max_length=300)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.region')),
            ],
            options={
                'ordering': ['number'],
                'permissions': (('can_edit', 'Manage car numbers'),),
            },
        ),
    ]
