from django.shortcuts import render
from django.urls import reverse
from .models import Item
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

# Create your views here.
#class based views

class ItemCreateView(CreateView):
    template_name = "ToDo/index.html"

class ItemListView(ListView):
    template_name = "ToDo/index.html"
    queryset = Item.objects.all()

class ItemUpdateView(UpdateView):
    template_name =  "ToDo/index.html"
    queryset = Item.objects.all()

class ItemDeleteView(DeleteView):
    template_name = "ToDo/index.html"
    queryset = Item.objects.all()

    def get_success_url(self):
        return reverse('todo:index')