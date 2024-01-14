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
    queryset = Item.objects.all()

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)

        if form.is_valid():
            # Process the form data and save it to the database
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']

            # Perform database operations here
            Item.objects.create(title = title, desc = desc)

            return render(request, self.template_name, {'form': form, 'success': True})

        return render(request, self.template_name, {'form': form})

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