from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .models import InputPhrase, ReferencePhrase, Prompt, Result
from .forms import UserRegistrationForm

# Представлення логіну
class UserLoginView(LoginView):
    template_name = 'login.html'


# ListViews
class InputPhraseListView(ListView):
    model = InputPhrase
    template_name = 'inputphrase_list.html'
    context_object_name = 'inputphrases'

class ReferencePhraseListView(ListView):
    model = ReferencePhrase
    template_name = 'referencephrase_list.html'
    context_object_name = 'referencephrases'

class PromptListView(ListView):
    model = Prompt
    template_name = 'prompt_list.html'
    context_object_name = 'prompts'

class ResultListView(ListView):
    model = Result
    template_name = 'result_list.html'
    context_object_name = 'results'


# Функції
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
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
