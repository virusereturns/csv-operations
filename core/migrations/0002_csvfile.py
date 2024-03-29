# Generated by Django 4.2 on 2024-02-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FilePathField(blank=True, null=True, path='media/csv')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('times_downloaded', models.IntegerField(default=0)),
                ('time_to_process', models.DurationField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CSV File',
                'verbose_name_plural': 'CSV Files',
                'ordering': ['-uploaded'],
            },
        ),
    ]
