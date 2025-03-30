from django.db import models

class LostItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='lost_images/')
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='found_images/')
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
