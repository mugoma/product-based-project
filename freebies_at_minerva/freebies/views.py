from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


from .models import Freebie

# Create your views here.


class FreebiesCreateView(CreateView):
    model = Freebie
    template_name = 'freebies/form.html'

    def get_success_url(self) -> str:
        return reverse('freebies:detail', args={"pk": self.get_object().pk})


class FreebiesListView(ListView):
    model = Freebie
    template_name = 'freebies/list.html'


class FreebiesDetailView(DetailView):
    model = Freebie
    template_name = 'freebies/detail.html'


class FreebiesUpdateView(UpdateView):
    model = Freebie
    template_name = 'freebies/form.html'

    def get_success_url(self) -> str:
        return reverse('freebies:detail', args={"pk": self.get_object().pk})


class FreebiesDeleteView(DeleteView):
    model = Freebie
    template_name = 'freebies/delete.html'
    form_class = None

    success_url = reverse_lazy('freebies:list')
