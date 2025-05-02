from django.shortcuts import render
from rest_framework import viewsets
from .models import InputPhrase, ReferencePhrase, Prompt, Result
from .serializers import InputPhraseSerializer, ReferencePhraseSerializer, PromptSerializer, ResultSerializer

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
