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
