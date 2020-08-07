from django.shortcuts import render

# Create your views here.

def home_page(request):
    
    return render(request, "index.html")


def photo_upload(request):


    return render(request,"photo_upload.html")




    