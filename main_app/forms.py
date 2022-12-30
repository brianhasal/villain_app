from django.forms import ModelForm
from .models import Surveillance

class SurveillanceForm(ModelForm):
  class Meta:
    model = Surveillance
    fields = ['date', 's_window']