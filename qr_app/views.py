from django.shortcuts import render
from .models import QR
# Create your views here.

def home(request):
    obj = QR.objects.all()

    context = {
        'obj':obj,
    }
    return render(request,'home.html',context)

