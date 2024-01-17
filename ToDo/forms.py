from django import forms

from ToDo.models import Item

class ItemForm(forms.ModelForm):
    title = forms.CharField(label="Item Title")
    desc = forms.CharField(label="Notes")

    class Meta:
        model = Item
        fields = ["title", "desc"]