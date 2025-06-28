from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter

from .views import (
    UserLoginView,
    InputPhraseListView,
    ReferencePhraseListView,
    PromptListView,
    ResultListView,
    register,
    index
)

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('inputphrases/', InputPhraseListView.as_view(), name='inputphrase_list'),
    path('referencephrases/', ReferencePhraseListView.as_view(), name='referencephrase_list'),
    path('prompts/', PromptListView.as_view(), name='prompt_list'),
    path('results/', ResultListView.as_view(), name='result_list'),
]
