from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import date

ESEA_CHOICES = (
    ('ESEA', (
            ('O', 'Open'),
            ('OI', 'Open + IM'),
            ('I', 'IM'),
            ('IN', 'IM + Invite'),
            ('N', 'Invite'),
            ('OIN', 'All')
        )
    ),
)

class Player(models.Model):
    class Meta:
        ordering = ['seasons', 'alias']
    
    user = models.OneToOneField(User)
    alias = models.CharField(max_length=32)
    classes = models.ManyToManyField('Class')
    esea = models.CharField(max_length=3, choices=ESEA_CHOICES, blank=True, null=True)
    eseaid = models.CharField(max_length=10, blank=True, null=True)
    seasons = models.PositiveSmallIntegerField()
    frags = models.ManyToManyField('Frag')
    days = models.CharField(max_length=7, blank=True, null=True)
    is_looking = models.BooleanField()
    
    def __unicode__(self):
        return '%s' % self.alias
    
class Class(models.Model):
    name = models.CharField(max_length=16)
    
    def __unicode__(self):
        return '%s' % self.name

class Frag(models.Model):
    fragger = models.OneToOneField(User)
    feedback = models.TextField()
    
    def __unicode__(self):
        return '%s' % self.fragger

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('alias', 'is_looking', 'seasons')
        #exclude = ('user', 'seasons', 'frags', 'esea', 'days')
    
    seasons = forms.ChoiceField(label="Seasons Experience", choices=(
        [('%s' % s, '%s' % s) for s in range(12)]
    ))
    days = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label="Days Available", choices=(
        ('S', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('R', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')
    ))
    eseaid = forms.CharField(required=False, label="ESEA User Number")
    esea = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label="ESEA Divisions Wanted", choices=(
        ('O', 'Open'), ('I', 'Intermediate'), ('N', 'Invite'),
    ))
    classes = forms.ModelMultipleChoiceField(queryset=Class.objects.all(), widget=forms.CheckboxSelectMultiple)
    
class FragForm(forms.ModelForm):
    class Meta:
        model = Frag
        exclude = ('fragger')