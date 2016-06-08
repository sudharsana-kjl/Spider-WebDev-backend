from django.forms import ModelForm
from .models import StudentForm

class NameForm(ModelForm):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #your_rollno = forms.IntegerField(label='Your rollno')
    #CHOICES=[('CSE','CSE'),
     #    ('ECE','ECE'),('EEE','EEE'),('CHEM','CHEM'),('ICE','ICE'),('PROD','PROD'),('META','META')]
   # your_dept = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    #your_email = forms.EmailField(label='Your email',max_length=100)
   # your_address = forms.CharField(label = 'Your address',max_length=200)
    #your_about = forms.CharField(label = 'Your about',max_length=300)


            class Meta:
	             model = StudentForm
	             fields = '__all__'
	#['your_name','your_rollno','your_dept','your_email','your_address','your_about']
    
    #def clean_email(self):

       # if (self.cleaned_data.get('your_email', '')
           # .endswith('@nitt.edu')):

            #raise ValidationError("Invalid email address.")

       # return self.cleaned_data.get('your_email', '')