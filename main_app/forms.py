from django.forms import ModelForm
from .models import Surveillance, Gang

class SurveillanceForm(ModelForm):
  class Meta:
    model = Surveillance
    fields = ['date', 'surveillance_Window']


class GangForm(ModelForm):
  class Meta:
    model = Gang
    fields = ['name', 'adjective']