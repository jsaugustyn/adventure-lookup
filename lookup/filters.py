from .models import Adventure, System, Terrain
import django_filters
from django import forms

class AdventureFilter(django_filters.FilterSet):
	system = django_filters.ModelMultipleChoiceFilter(queryset=System.objects.all(),
        widget=forms.CheckboxSelectMultiple)
	terrain = django_filters.ModelMultipleChoiceFilter(queryset=Terrain.objects.all(),
        widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Adventure
		fields = ['system','terrain']