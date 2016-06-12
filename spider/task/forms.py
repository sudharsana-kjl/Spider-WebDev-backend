from django import forms
from .models import StudentForm,SearchModel,EditModel


class NameForm(forms.ModelForm):
            class Meta:
                   model = StudentForm
                   fields = '__all__'
                   widgets = {'passcode': forms.HiddenInput()}

                   
      #['your_name','your_rollno','your_dept','your_email','your_address','your_about']
    

class SearchForm(forms.ModelForm):
            class Meta:
                  model = SearchModel
                  fields = '__all__'


class EditForm(forms.ModelForm):
            class Meta:
                  model = StudentForm
                  exclude = ['your_rollno']
                  widgets = {'passcode': forms.HiddenInput()}

class PassForm(forms.ModelForm):
            class Meta:
                  model = EditModel
                  fields='__all__'

            #class Meta:
            #     model = StudentForm
            #     fields = ['your_rollno']
