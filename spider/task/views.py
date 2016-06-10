
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render

from .forms import NameForm,SearchForm
from .models import StudentForm

def index(request):
    
    if request.method == 'POST':
        
       form = NameForm(request.POST or None)
       if form.is_valid():
           m = form.save(commit='False')
           passcode = StudentForm.get('passcode')
           m.save()

           return render(request,'task/thanks.html',)

    else:
        form = NameForm()

    return render(request, 'task/index.html', {'form': form},)

def searchStud(request):
    
    if request.method == 'GET':

      form = SearchForm(request.GET or None)

      if form.is_valid():

         s_query = form.cleaned_data['search_query']
         s_results = StudentForm.objects.filter(your_rollno=s_query)
         if not s_results:
           return HttpResponse("<h1>Not Available</h1>")          
         else:
           return render(request,'task/thanks.html',{'object_list':s_results}) 
    else:
        form = SearchForm()
  
    #return render(request, 'task/index.html', {'form': form,})
    return render(request,'task/search.html',{'form': form},)





            
            