from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.forms import BaseModelForm
from ToDo.forms import ItemForm
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
    template_name = "ToDo/item_create.html"
    form_class = ItemForm
    queryset = Item.objects.all()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)

class ItemListView(ListView):
    template_name = "ToDo/index.html"
    queryset = Item.objects.all()

class ItemUpdateView(UpdateView):
    template_name =  "ToDo/item_update.html"
    queryset = Item.objects.all()

class ItemDeleteView(DeleteView):
    template_name = "ToDo/item_delete.html"
    queryset = Item.objects.all()

    def get_success_url(self):
        return reverse('todo:index')