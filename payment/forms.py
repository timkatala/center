from dal import autocomplete

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Student
        fields = ('__all__')