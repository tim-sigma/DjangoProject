# Generated by Django 5.1.5 on 2025-03-01 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputPhrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferencePhrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('input_phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.inputphrase')),
                ('reference_phrases', models.ManyToManyField(to='main_app.referencephrase')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField()),
                ('similarity_ml', models.FloatField(blank=True, null=True)),
                ('similarity_cosine', models.FloatField(blank=True, null=True)),
                ('similarity_semantic', models.FloatField(blank=True, null=True)),
                ('similarity_contextual', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('input_phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.inputphrase')),
                ('matched_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.referencephrase')),
                ('prompt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.prompt')),
            ],
        ),
    ]
