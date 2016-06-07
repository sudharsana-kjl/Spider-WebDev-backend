
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
           
            NameForm.save()
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'task/index.html', {'form': form})

def thanks(request):
	return render(request,'task/thanks.html',)