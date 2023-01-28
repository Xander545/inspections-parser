# Generated by Django 4.1.5 on 2023-01-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_inspectionsource_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection',
            old_name='insection_date',
            new_name='inspection_date',
        ),
        migrations.AddField(
            model_name='inspection',
            name='inspection_place',
            field=models.CharField(default='no place', max_length=200),
        ),
    ]