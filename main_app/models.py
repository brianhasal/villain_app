from django.db import models
from django.urls import reverse

# Create your models here.

class Villain(models.Model):
  name = models.CharField(max_length=100)
  identity = models.CharField(max_length=100)
  badness_scale = models.IntegerField()
  nemeses = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'villain_id': self.id })



