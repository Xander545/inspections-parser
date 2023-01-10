# Generated by Django 4.1.5 on 2023-01-08 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField(verbose_name='Count rows of loading')),
                ('company_name', models.CharField(max_length=200)),
                ('head_of_company', models.CharField(max_length=200)),
                ('phones', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('address_in_law', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InspectionSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InspectionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InspectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='insection_id',
        ),
        migrations.AddField(
            model_name='inspection',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='insection_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of inspecting'),
        ),
        migrations.CreateModel(
            name='InspectionLoadHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_date', models.DateTimeField(verbose_name='Loading datetime')),
                ('count_rows', models.IntegerField(verbose_name='Count rows of loading')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.inspectionsource')),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='company',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.company'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='region',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.region'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='source',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.inspectionsource'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='status',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.inspectionstatus'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='type',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.inspectiontype'),
        ),
    ]
