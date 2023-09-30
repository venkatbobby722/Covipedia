from django import forms
from calc.models import blog

class ResourceForm(forms.ModelForm):
  class Meta:
      model = blog
      fields = '__all__'
