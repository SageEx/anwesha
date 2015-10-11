from django.shortcuts import render
from django.shortcuts import *
from django.http import *
from django.template import *
from reg.models import *
from django.core import serializers

# Create your views here.
def home(request):
    # p = People.objects.all()
    # data = serializers.serialize('json', p)
    return HttpResponse("hello arindam!")

    # template = loader.get_template('home.html')
    # context=RequestContext(request)
    # return render(request,'home.html')
    # return HttpResponse(template.render(context))
