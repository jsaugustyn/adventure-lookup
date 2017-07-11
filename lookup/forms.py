from django.forms import ModelForm
from .models import Adventure

class AdventureForm(ModelForm):
	class Meta:
		model = Adventure
		fields = ['adv_title','adv_desc', 'min_party_size','max_party_size','min_level','max_level','adv_availability','adv_cost','system','terrain','publication_year','author','source','source_url','page_count']

class AdventureEdit(ModelForm):
	class Meta:
		model = Adventure
		fields = ['adv_title','adv_desc', 'min_party_size','max_party_size','min_level','max_level','adv_availability','adv_cost','system','terrain','publication_year','author','source','source_url','page_count']
