from django import forms
from.models import WorkModel

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')
    
class WorkRecordForm(forms.ModelForm):
    class Meta:
        model = WorkModel
        fields = ['workingDate', 'workNumber', 'memo', 'workStartTime', 'workEndTime']
        
        widgets = {
            'workingDate': forms.SelectDateWidget,
            'workStartTime':forms.DateTimeInput
        }

class FindForm(forms.Form):
    find = forms.CharField(label='find', required=False)