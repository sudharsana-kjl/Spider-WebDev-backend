#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
   #return HttpResponse("<h1>Hey there!</h1>")
   #from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            NameForm.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'task/index.html', {'form': form})

def thanks(request):
	return render(request,'task/thanks.html',)