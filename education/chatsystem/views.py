from django.shortcuts import render

# Create your views here.

def chatapp(requset):
    template_name = "Community_page/chatScreen.html"
    return render(requset, template_name)