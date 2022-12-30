from django.db import models
from django.urls import reverse

SWINDOWS = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening'),
  ('N', 'Night')
)

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

class Surveillance(models.Model):
  date = models.DateField('Surveillance Date')
  surveillance_Window = models.CharField(
    max_length=1,
    choices=SWINDOWS,
    default=SWINDOWS[0][0]
  )

  villain = models.ForeignKey(Villain, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_surveillance_Window_display()} on {self.date}"






