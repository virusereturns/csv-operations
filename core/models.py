from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['name']


class StoredFile(models.Model):
    class FILETYPES(models.TextChoices):
        CSV = 'csv', 'csv'
        XLSX = 'xlsx', 'xlsx'
    
    class STATUS(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSING = 'processing', 'Processing'
        DONE = 'done', 'Done'

    file = models.FilePathField(path='media/filestorage', blank=True, null=True)
    filetype = models.CharField(max_length=5, choices=FILETYPES.choices, default=FILETYPES.CSV)
    created = models.DateTimeField(auto_now_add=True)
    times_downloaded = models.IntegerField(default=0)
    time_to_process = models.DurationField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS.choices, default=STATUS.PENDING)

    def __str__(self):
        return f'File id: {self.id}'

    def download(self):
        self.times_downloaded += 1
        self.save()

    class Meta:
        verbose_name = 'CSV File'
        verbose_name_plural = 'CSV Files'
        ordering = ['-created']
