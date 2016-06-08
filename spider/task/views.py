
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .models import StudentForm

def index(request):
    
    if request.method == 'POST':
        
        form = NameForm(request.POST)
        if form.is_valid():
           # NameForm.clean_email()
           #your_name = request.POST.get('your_name','')
           #your_rollno = request.POST.get('your_rollno','')
           #your_dept = request.POST.get('your_dept','')
           #your_email = request.POST.get('your_email','')
           #your_address = request.POST.get('your_address','')
           #your_about = request.POST.get('your_about','')
           #m= StudentForm(your_name= your_name,your_rollno = your_rollno,your_dept=your_dept,your_email=your_email,your_address=your_address,your_about=your_about)
           m = form.save(commit=False)
           m.save()
           return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'task/index.html', {'form': form})

def thanks(request):
	return render(request,'task/thanks.html',)