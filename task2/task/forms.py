from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_rollno = forms.IntegerField(label='Your rollno')
    CHOICES=[('CSE','CSE'),
         ('ECE','ECE'),('EEE','EEE'),('CHEM','CHEM'),('ICE','ICE'),('PROD','PROD'),('META','META')]
    your_dept = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    your_email = forms.EmailField(label='Your email',max_length=100)
    your_address = forms.CharField(label = 'Your address',max_length=200)
    your_about = forms.CharField(label = 'Your about',max_length=300)


 