from testapp.models import Info
from django import forms
class Info_Form(forms.ModelForm):
    class Meta:
        model=Info
        fields='__all__'

class Download_Form(forms.Form):
    link=forms.CharField()
