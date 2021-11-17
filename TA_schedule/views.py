from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, "home.html", {'title': 'Home'})

    # def post(self,request):
    #     return render(request,"home.html",{"days":Days.choices,"sections":Sections.choices})
