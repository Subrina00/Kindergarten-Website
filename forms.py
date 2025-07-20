from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['full_name', 'date_of_birth', 'mother_name', 'father_name',
                  'address', 'photo', 'email', 'mobile_no', 'class_to_admit']
