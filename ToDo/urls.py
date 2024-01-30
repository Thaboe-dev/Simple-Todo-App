from django.urls import path
from .views import (
    CompleteItemListView,
    EditStatusView,
    ItemCreateView,
    ItemDeleteView,
    ItemListView,
    ItemUpdateView,
)

app_name = 'todo'
urlpatterns = [
    path("", ItemListView.as_view(), name="home"),
    path("complete/", CompleteItemListView.as_view(), name="item-complete"),
    path("create/", ItemCreateView, name="item-create"),
    path("<int:id>/status/",EditStatusView, name="item-status"),
    path("<int:id>/update/", ItemUpdateView, name="item-update"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
]