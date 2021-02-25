from django.shortcuts import render
from .forms import imgform
from .models import imageTable
# Create your views here.

def index(request):
    if request.method == "POST":
        form = imgform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = imgform()
    img = imageTable.objects.all()
    return render(request,'index.html',{'form':form,'img':img});