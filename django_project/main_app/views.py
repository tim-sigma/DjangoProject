from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import InputPhrase, ReferencePhrase, Prompt, Result
from .serializers import InputPhraseSerializer, ReferencePhraseSerializer, PromptSerializer, ResultSerializer
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

class InputPhraseViewSet(viewsets.ModelViewSet):
    queryset = InputPhrase.objects.all()
    serializer_class = InputPhraseSerializer

class ReferencePhraseViewSet(viewsets.ModelViewSet):
    queryset = ReferencePhrase.objects.all()
    serializer_class = ReferencePhraseSerializer

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class UserLoginView(LoginView):
    template_name = 'login.html'


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # login(request, user)
            return redirect('home') # реалізувати home
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
