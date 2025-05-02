from rest_framework import serializers
from .models import InputPhrase, ReferencePhrase, Prompt, Result

class InputPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputPhrase
        fields = '__all__'

class ReferencePhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferencePhrase
        fields = '__all__'

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
