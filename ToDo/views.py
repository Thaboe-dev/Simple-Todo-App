from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.forms import BaseModelForm
from ToDo.forms import ItemForm
from .models import Item
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

# Create your views here.
#class based views

def ItemCreateView(request):
    form = ItemForm(request.POST)

    if form.is_valid():
        # Process the form data and save it to the database
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']

            # Perform database operations here
            Item.objects.create(title = title, desc = desc)
            #success message
            messages.success(request, "Item created successfully")
            return redirect("http://127.0.0.1:8000/todo/")

    return render(request, "ToDo/item_create.html")

class ItemListView(ListView):
    template_name = "ToDo/index.html"
    queryset = Item.objects.filter(status = "Pending")

def ItemUpdateView(request, id):
    obj = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST, instance = obj)

    if form.is_valid():
        # Process the form data and save it to the database
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']

            # Perform database operations here
            obj.title = title
            obj.desc = desc
            obj.save()
            #success message
            messages.success(request, "Item updated successfully")
            return redirect(obj)

    return render(request, "ToDo/item_update.html", context={"object":obj})

class ItemDeleteView(SuccessMessageMixin, DeleteView):
    template_name = "ToDo/item_delete.html"
    queryset = Item.objects.all()
    success_message = "The Item was deleted successfully"

    def get_success_url(self):
        return reverse('todo:home')
    
class CompleteItemListView(ListView):
    template_name = "ToDo/complete.html"
    queryset = Item.objects.filter(status = "Complete")