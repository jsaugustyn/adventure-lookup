from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Adventure
from .filters import AdventureFilter
from .forms import AdventureForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def index(request):
#    adventure_list = Adventure.objects.all()
#    context = {'adventure_list': adventure_list}
    #adventure_filter = AdventureFilter(request.GET, queryset=adventure_list)
#    return render(request, 'lookup/index.html', context)
	#return render(request, 'lookup/index.html', {'filter': adventure_filter})
	

#def search(request):
#	adventure_list = Adventure.objects.all()
#	adventure_filter = AdventureFilter(request.GET, queryset=adventure_list)
#	return render(request, 'search/adventure_list.html', {'filter': adventure_filter})

class AdventureView(ListView):
#	queryset = Adventure.objects.order_by('-pub_date')
#	context_object_name = 'adventure_list'
#	template_name = 'lookup/index.html'

	model = Adventure
	template_name = 'lookup/index.html'

	@staticmethod
	def _get_adventure_page(adventure_list, page):
		paginator = Paginator(adventure_list, 5)
		try:
			adventure_list = paginator.page(page)
		except PageNotAnInteger:
			adventure_list = paginator.page(1)
		except EmptyPage:
			adventure_list = paginator.page(paginator.num_pages)
		return adventure_list

	def get_context_data(self, **kwargs):
            context = super().get_context_data()
            adventure_list = Adventure.objects.order_by('-pub_date').all()
            adventure_filter = AdventureFilter(self.request.GET, queryset=adventure_list)
            context['adventure_list'] = self._get_adventure_page(adventure_filter.qs,
                                                     self.request.GET.get('page'))
            context['adventure_filter'] = adventure_filter
            return context

class AdventureDetailView(DetailView):
	model = Adventure

class AddAdventure(CreateView):
	model = Adventure
	form_class = AdventureForm
	success_url = reverse_lazy('index')
	def form_valid(self, form):
		form.instance.submitted_by = self.request.user
		return super().form_valid(form)
	

class AdventureUpdate(UpdateView):
	model=Adventure
	form_class = AdventureForm
	success_url = reverse_lazy('index')

class AdventureDelete(DeleteView):
	model=Adventure
	success_url = reverse_lazy('index')