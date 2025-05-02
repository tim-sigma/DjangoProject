from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InputPhraseViewSet, ReferencePhraseViewSet, PromptViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'inputphrases', InputPhraseViewSet)
router.register(r'referencephrases', ReferencePhraseViewSet)
router.register(r'prompts', PromptViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
