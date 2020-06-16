from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from .models import WorkModel

def index(request):
    # params = {
    #     'title' : 'Hello',
    #     'message' : 'Your Data',
    #     'form' : HelloForm()
    # }
    
    # if (request.method == 'POST'):
    #     params['message'] = '名前: ' + request.POST['name'] + \
    #         '<br>メール: ' + request.POST['mail'] + \
    #         '<br>年齢: ' + request.POST['age']
    #     params['form'] = HelloForm(request.POST)
    # return render(request, 'workrecord/index.html', params)
    
    data = WorkModel.objects.all()
    params = {
        'title' : 'WorkRecord',
        'message' : 'All Record',
        'data' : data
    }
    return render(request, 'workrecord/index.html', params)