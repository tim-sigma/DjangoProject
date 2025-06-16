from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from .views import InputPhraseViewSet, ReferencePhraseViewSet, PromptViewSet, ResultViewSet, register, index, UserLoginView

router = DefaultRouter()
router.register(r'inputphrases', InputPhraseViewSet)
router.register(r'referencephrases', ReferencePhraseViewSet)
router.register(r'prompts', PromptViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
