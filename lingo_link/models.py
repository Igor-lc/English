from django.db import models
from django.core.exceptions import ValidationError
from spellchecker import SpellChecker
import enchant
import re


def validate_ru_SpellChecker(value):
    spell = SpellChecker(language='ru')
    words = [word.strip() for word in re.split(r'[,\s]+', value)]
    for word in words:
        if not spell.correction(word):
            raise ValidationError(f"Misspelled word: {word}")


def validate_english_SpellChecker(value):
    spell = SpellChecker(language='en')
    words = [word.strip() for word in re.split(r'[,\s]+', value)]
    for word in words:
        if not spell.correction(word):
            raise ValidationError(f"Misspelled word: {word}")


def validate_english_enchant(value):
    dictionary = enchant.Dict("en_US")
    words = [word.strip() for word in re.split(r'[,\s]+', value)]
    for word in words:
        if not dictionary.check(word):
            raise ValidationError(f"Misspelled word: {word}")

class Verb(models.Model):
    PARTS_OF_SPEECH_CHOICES = [
        ('RegularVerbs', 'Regular Verbs'),
        ('IrregularVerbs', 'Irregular Verbs'),
        ('PhrasalVerbs', 'Phrasal Verbs'),
        ('PerfectiveVerbs', 'Perfective Verbs'),
        ('ImperfectiveVerbs', 'Imperfective Verbs'),
        ('ModalVerbs', 'Modal Verbs'),
        ('Gerunds', 'Gerunds'),
        ('Irregular_Forms', 'Irregular Forms'),
        ('PassiveVerbs', 'Passive Verbs'),
        ('InvariableVerbs', 'Invariable Verbs')
    ]

    id = models.AutoField(primary_key=True)
    ru_past_present_future = models.CharField(max_length=97, blank=False, validators=[validate_ru_SpellChecker])
    eng_past_present_future = models.CharField(max_length=139, blank=False, validators=[validate_english_SpellChecker, validate_english_enchant])
    type = models.TextField(choices=PARTS_OF_SPEECH_CHOICES, blank=False)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'Verbs'
        db_table = 'verbs'

class SpeechPart(models.Model):
    PARTS_OF_SPEECH_CHOICES = [
        ('Noun', 'Noun'),
        ('Adjective', 'Adjective'),
        ('Participle', 'Participle'),
        ('Pronoun', 'Pronoun'),
        ('Adverb', 'Adverb'),
        ('Preposition', 'Preposition'),
        ('Conjunction', 'Conjunction'),
        ('Interjection', 'Interjection'),
        ('Particle', 'Particle'),
        ('Parenthetical Expression', 'Parenthetical Expression')
    ]

    id = models.AutoField(primary_key=True)
    ru = models.CharField(max_length=31, blank=False, validators=[validate_ru_SpellChecker])
    eng = models.CharField(max_length=45, blank=False, validators=[validate_english_SpellChecker, validate_english_enchant])
    type = models.TextField(choices=PARTS_OF_SPEECH_CHOICES, blank=False)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'Speech Parts'
        db_table = 'speech_parts'

class Synonym(models.Model):
    id = models.AutoField(primary_key=True)
    ru_synonyms = models.TextField(blank=False, validators=[validate_ru_SpellChecker])
    eng_synonyms = models.TextField(blank=False, validators=[validate_english_SpellChecker, validate_english_enchant])

    class Meta:
        verbose_name_plural = 'Synonyms'
        db_table = 'synonyms'