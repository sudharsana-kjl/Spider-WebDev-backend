from django.forms import ModelForm
from .models import StudentForm,SearchModel

class NameForm(ModelForm):
            class Meta:
	             model = StudentForm
	             exclude = ['your_code']
	#['your_name','your_rollno','your_dept','your_email','your_address','your_about']
    

class SearchForm(ModelForm):
            class Meta:
            	model = SearchModel
            	fields = '__all__'

            #class Meta:
            #	model = StudentForm
            #	fields = ['your_rollno']
