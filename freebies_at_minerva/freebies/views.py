from typing import Any, Dict
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


from .models import Freebie

# Create your views here.


class FreebiesFormMixin:
    model = Freebie
    template_name = 'freebies/form.html'
    fields = ['title', 'description', 'percentage_off', 'amount_off', 'city']
    page_context = None

    def get_success_url(self) -> str:
        return reverse('freebies:detail', args=[self.object.pk])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['page_context'] = self.page_context
        return data


class FreebiesCreateView(FreebiesFormMixin, CreateView):
    page_context = 'Create'


class FreebiesListView(ListView):
    model = Freebie
    template_name = 'freebies/list.html'


class FreebiesDetailView(DetailView):
    model = Freebie
    template_name = 'freebies/detail.html'


class FreebiesUpdateView(FreebiesFormMixin, UpdateView):
    page_context = 'Update'


class FreebiesDeleteView(DeleteView):
    model = Freebie
    template_name = 'freebies/delete.html'

    success_url = reverse_lazy('freebies:list')
