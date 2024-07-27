from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
def member(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('member.html')
    data1 = {
        "mymembers":mymembers,
               }
    return HttpResponse(template.render(data1,request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template=loader.get_template("details.html")
    context={
        "mymember":mymember
    }
    return HttpResponse(template.render(context,request))