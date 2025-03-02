from django.db.models import Model, TextField, CharField, ForeignKey, ManyToManyField, FloatField, DateTimeField, CASCADE

# Модель Вхідна фраза
class InputPhrase(Model):
    text = CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.text

# Модель Опорна фраза
class ReferencePhrase(Model):
    text = CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.text

# Модель Промпт
class Prompt(Model):
    input_phrase = ForeignKey(InputPhrase, on_delete=CASCADE)
    reference_phrases = ManyToManyField(ReferencePhrase)
    text = TextField()
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Промпт фрази: {self.input_phrase.text}"

# Модель Результат
class Result(Model):
    input_phrase = ForeignKey(InputPhrase, on_delete=CASCADE)
    prompt = ForeignKey(Prompt, on_delete=CASCADE)
    matched_reference = ForeignKey(ReferencePhrase, on_delete=CASCADE)
    explanation = TextField()
    similarity_ml = FloatField(null=True, blank=True)
    similarity_cosine = FloatField(null=True, blank=True)
    similarity_semantic = FloatField(null=True, blank=True)
    similarity_contextual = FloatField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Результат для фрази: {self.input_phrase.text}"

