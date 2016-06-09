from django.forms import ModelForm
from .models import StudentForm

class NameForm(ModelForm):
            class Meta:
	             model = StudentForm
	             fields = '__all__'
	#['your_name','your_rollno','your_dept','your_email','your_address','your_about']
    
            def clean_email(self):

                if (self.cleaned_data.get('your_email', '').endswith('@nitt.edu')):

                   raise ValidationError("Invalid email address.")

                return self.cleaned_data.get('your_email', '')