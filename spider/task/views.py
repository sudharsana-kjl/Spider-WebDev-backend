
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404

from .forms import NameForm,SearchForm,EditForm,PassForm
from .models import StudentForm
from django.utils.crypto import get_random_string

def index(request):
    
    if request.method == 'POST':
        
       form = NameForm(request.POST or None)

       if form.is_valid():
           m = form.save(commit='False')
           pcode = get_random_string(length=6)
           m.passcode = pcode
           m.save()

           return render(request,'task/thanks.html',{'pcode':pcode})

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
  
    
    return render(request,'task/search.html',{'form': form},)

def editStud(request,id=None):

    instance = get_object_or_404(StudentForm,id=id)
    
    rollno = instance.your_rollno
    passcd = instance.passcode
    form = EditForm(request.POST or None,instance=instance)
    forms = PassForm(request.POST or None)
    
    if request.method == 'POST':
        
        form = EditForm(request.POST or None,instance=instance)
        forms = PassForm(request.POST or None)

       

        if form.is_valid() and forms.is_valid():
          pacode = forms.cleaned_data['passcod']
          
          if pacode == passcd:
            
            instance = form.save(commit=False)
       
            instance.save()
            return render(request,'task/thanksedit.html',)
          else:
            return render(request,'task/editfail.html',)
       
        else:
          return render(request,'task/edit.html',{'form':form,'forms':forms,'instance':instance,'rollno':rollno}),
  

    return render(request,'task/edit.html',{'form':form,'forms':forms,'instance':instance,'rollno':rollno},)

  






            
            