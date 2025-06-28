from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import InputPhraseViewSet, ReferencePhraseViewSet, PromptViewSet, ResultViewSet

router = DefaultRouter()
router.register('inputphrases', InputPhraseViewSet)
router.register('referencephrases', ReferencePhraseViewSet)
router.register('prompts', PromptViewSet)
router.register('results', ResultViewSet)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
