
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .models import StudentForm

def index(request):
    
    if request.method == 'POST':
        
       form = NameForm(request.POST or None)
       if form.is_valid():
           m = form.save(commit='False')
           name = form.cleaned_data['name']
           
           m = StudentForm.objects.create(name=name)
           m.save()

           return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'task/index.html', {'form': form},)

def thanks(request):
	return render(request,'task/thanks.html',)