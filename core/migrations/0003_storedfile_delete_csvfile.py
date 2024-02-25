# Generated by Django 4.2 on 2024-02-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_csvfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FilePathField(blank=True, null=True, path='media/filestorage')),
                ('filetype', models.CharField(choices=[('csv', 'csv'), ('xlsx', 'xlsx')], default='csv', max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('times_downloaded', models.IntegerField(default=0)),
                ('time_to_process', models.DurationField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CSV File',
                'verbose_name_plural': 'CSV Files',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='CsvFile',
        ),
    ]