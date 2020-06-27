from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import HelloForm
from .forms import WorkRecordForm
from .models import WorkModel
from .forms import FindForm

def index(request):
    
    data = WorkModel.objects.all()
    params = {
        'title' : 'WorkRecord',
        'message' : 'All Record',
        'data' : data
    }
    return render(request, 'workrecord/index.html', params)

#create model
def create(request):
    if(request.method == 'POST'):
        obj = WorkModel()
        workRecordForm = WorkRecordForm(request.POST, instance=obj)
        workRecordForm.save()
        return redirect(to='/')
    
    params = {
        'title' : 'WorkRecord',
        'form' : WorkRecordForm()
    }
    
    return render(request, 'workrecord/create.html', params)

def find(request):
    
    form = FindForm()

    data = WorkModel.objects.all()
    params = {
        'title' : 'WorkRecord',
        'message' : 'creating now',
        'form' : form,
        'data' : data
    }
    return render(request, 'workrecord/index.html', params)