from django.contrib import admin
from lingo_link.models import Verb, SpeechPart, Synonym


@admin.register(Verb)  # Реєстрація моделі у адмінці
class VerbEntryAdmin(admin.ModelAdmin):
    list_display = ('ru_past_present_future', 'eng_past_present_future', 'type')
    search_fields = ('ru_past_present_future', 'eng_past_present_future', 'type')
    list_filter = ('type',)

@admin.register(SpeechPart)
class SpeechPartAdmin(admin.ModelAdmin):
    list_display = ('ru', 'eng', 'type')
    search_fields = ('ru', 'eng', 'type')
    list_filter = ('type',)


@admin.register(Synonym)
class WordSynonymAdmin(admin.ModelAdmin):
    list_display = ('ru_synonyms', 'eng_synonyms')
    search_fields = ('ru_synonyms', 'eng_synonyms')