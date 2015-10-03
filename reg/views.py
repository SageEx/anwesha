from django.shortcuts import render
from django.shortcuts import *
from django.http import *
from django.template import *
from reg.models import *

# Create your views here.
def home(request):
    p = People.objects.get(pid=1)
    return HttpResponse('home.html'+str(p))

    # template = loader.get_template('home.html')
    # context=RequestContext(request)
    # return render(request,'home.html')
    # return HttpResponse(template.render(context))
