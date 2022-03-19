from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class VRegristation(View):

    def get(self,request):

        form = UserCreationForm()

        return render(request, 'registration/registration.html', {'form' : form})

    def post(self, request):

        pass