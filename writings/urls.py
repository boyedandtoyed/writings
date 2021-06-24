from django.urls import path
from . import views

app_name = "writings"

urlpatterns = [
    path('add/',views.create_writing, name="create"),
    path("update/", views.update_writings, name="update"),
    path('delete/', views.delete_writings, name="delete"),
    path('show-writing/<slug:slug>', views.show_writing, name='show_writing'),
    path('my-writings/', views.my_writings, name="my_writings"),
]
