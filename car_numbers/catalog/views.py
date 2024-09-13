from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import is_valid_path
from django.views import generic
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required()
def index(request):
    form = SearchForm(request.GET)
    object_list = None
    if form.is_valid():
        query = form.cleaned_data['query'].lower()
        object_list = Plate.objects.filter(number__icontains=query)

    return render(
        request,
        'catalog/index.html',
        context={
            'request': request,
            'form': form,
            'object_list': object_list
        }
    )

class AllListView(LoginRequiredMixin, generic.ListView):
    model = Plate
    paginate_by = 6

class PlateDetailView(LoginRequiredMixin, generic.DetailView):
    model = Plate

class PlateCreate(LoginRequiredMixin, generic.CreateView):
    model = Plate
    form_class = PlateCreateForm
    template_name = 'catalog/model_form.html'
    extra_context = {
        'title': 'Добавить номер'
    }

    def clean(self):
        cleaned_data = super().clean()
    def get_success_url(self):
        return reverse_lazy('add-plate') + '?success_add=True'

class PlateUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Plate
    fields = ['owner', 'car', 'notes']
    template_name = 'catalog/model_form.html'

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.object.id])

class PlateDelete(LoginRequiredMixin, generic.DeleteView):
    model = Plate

    def get_success_url(self):
        return reverse_lazy('index')

class RegionList(LoginRequiredMixin, generic.ListView):
    model = Region

class RegionCreate(LoginRequiredMixin, generic.CreateView):
    model = Region
    template_name = 'catalog/model_form.html'
    fields = '__all__'
    extra_context = {
        'title': 'Добавить регион',
    }

    def get_success_url(self):
        return reverse_lazy('region-list')

class RegionUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Region
    fields = '__all__'
    template_name = 'catalog/model_form.html'

    def get_success_url(self):
        return reverse_lazy('region-list')
