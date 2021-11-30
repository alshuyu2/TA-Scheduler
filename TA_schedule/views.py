from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        return render(request, "login.html")


class DashBoard(View):
    def get(self, request):
        return render(request, "dashboard.html")

    def post(self, request):
        return render(request, "dashboard.html")
