from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .models import InputPhrase, ReferencePhrase, Prompt, Result
from .forms import UserRegistrationForm

# Представлення логіну
class UserLoginView(LoginView):
    template_name = 'login.html'


# CreateViews
class InputPhraseCreateView(CreateView):
    model = InputPhrase
    fields = ['text']
    template_name = 'create_form.html'
    success_url = '/inputphrases/'

class ReferencePhraseCreateView(CreateView):
    model = ReferencePhrase
    fields = ['text']
    template_name = 'create_form.html'
    success_url = '/referencephrases/'

class PromptCreateView(CreateView):
    model = Prompt
    fields = ['input_phrase', 'reference_phrases', 'text']
    template_name = 'create_form.html'
    success_url = '/prompts/'

class ResultCreateView(CreateView):
    model = Result
    fields = [
        'input_phrase', 'prompt', 'matched_reference',
        'explanation', 'similarity_ml', 'similarity_cosine',
        'similarity_semantic', 'similarity_contextual'
    ]
    template_name = 'create_form.html'
    success_url = '/results/'


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


# DetailViews
class InputPhraseDetailView(DetailView):
    model = InputPhrase
    template_name = 'inputphrase_detail.html'
    context_object_name = 'inputphrase'

class ReferencePhraseDetailView(DetailView):
    model = ReferencePhrase
    template_name = 'referencephrase_detail.html'
    context_object_name = 'referencephrase'

class PromptDetailView(DetailView):
    model = Prompt
    template_name = 'prompt_detail.html'
    context_object_name = 'prompt'

class ResultDetailView(DetailView):
    model = Result
    template_name = 'result_detail.html'
    context_object_name = 'result'


# UpdateViews
class InputPhraseUpdateView(UpdateView):
    model = InputPhrase
    fields = ['text']
    template_name = 'update_form.html'
    success_url = '/inputphrases/'

class ReferencePhraseUpdateView(UpdateView):
    model = ReferencePhrase
    fields = ['text']
    template_name = 'update_form.html'
    success_url = '/referencephrases/'

class PromptUpdateView(UpdateView):
    model = Prompt
    fields = ['input_phrase', 'reference_phrases', 'text']
    template_name = 'update_form.html'
    success_url = '/prompts/'

class ResultUpdateView(UpdateView):
    model = Result
    fields = [
        'input_phrase', 'prompt', 'matched_reference',
        'explanation', 'similarity_ml', 'similarity_cosine',
        'similarity_semantic', 'similarity_contextual'
    ]
    template_name = 'update_form.html'
    success_url = '/results/'


# DeleteViews
class InputPhraseDeleteView(DeleteView):
    model = InputPhrase
    template_name = 'confirm_delete.html'
    success_url = '/inputphrases/'

class ReferencePhraseDeleteView(DeleteView):
    model = ReferencePhrase
    template_name = 'confirm_delete.html'
    success_url = '/referencephrases/'

class PromptDeleteView(DeleteView):
    model = Prompt
    template_name = 'confirm_delete.html'
    success_url = '/prompts/'

class ResultDeleteView(DeleteView):
    model = Result
    template_name = 'confirm_delete.html'
    success_url = '/results/'


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
