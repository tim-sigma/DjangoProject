from django.urls import path
from django.contrib.auth.views import LogoutView

import main_app.views as views


urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

# CreateViews
urlpatterns += [
    path('inputphrases/add/', views.InputPhraseCreateView.as_view(), name='inputphrase_add'),
    path('referencephrases/add/', views.ReferencePhraseCreateView.as_view(), name='referencephrase_add'),
    path('prompts/add/', views.PromptCreateView.as_view(), name='prompt_add'),
    path('results/add/', views.ResultCreateView.as_view(), name='result_add'),
]

# ListViews
urlpatterns += [
    path('inputphrases/', views.InputPhraseListView.as_view(), name='inputphrase_list'),
    path('referencephrases/', views.ReferencePhraseListView.as_view(), name='referencephrase_list'),
    path('prompts/', views.PromptListView.as_view(), name='prompt_list'),
    path('results/', views.ResultListView.as_view(), name='result_list'),
]

# DetailViews
urlpatterns += [
    path('inputphrases/<int:pk>/', views.InputPhraseDetailView.as_view(), name='inputphrase_detail'),
    path('referencephrases/<int:pk>/', views.ReferencePhraseDetailView.as_view(), name='referencephrase_detail'),
    path('prompts/<int:pk>/', views.PromptDetailView.as_view(), name='prompt_detail'),
    path('results/<int:pk>/', views.ResultDetailView.as_view(), name='result_detail'),
]

# UpdateViews
urlpatterns += [
    path('inputphrases/<int:pk>/edit/', views.InputPhraseUpdateView.as_view(), name='inputphrase_edit'),
    path('referencephrases/<int:pk>/edit/', views.ReferencePhraseUpdateView.as_view(), name='referencephrase_edit'),
    path('prompts/<int:pk>/edit/', views.PromptUpdateView.as_view(), name='prompt_edit'),
    path('results/<int:pk>/edit/', views.ResultUpdateView.as_view(), name='result_edit'),
]

# DeleteViews
urlpatterns += [
    path('inputphrases/<int:pk>/delete/', views.InputPhraseDeleteView.as_view(), name='inputphrase_delete'),
    path('referencephrases/<int:pk>/delete/', views.ReferencePhraseDeleteView.as_view(), name='referencephrase_delete'),
    path('prompts/<int:pk>/delete/', views.PromptDeleteView.as_view(), name='prompt_delete'),
    path('results/<int:pk>/delete/', views.ResultDeleteView.as_view(), name='result_delete'),
]
