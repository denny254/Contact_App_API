from django.urls import path 
from.views import ContactList, ContactDetailView


urlpatterns = [
    path('',  ContactList.as_view()),
    path('<int:pk>',  ContactDetailView.as_view())
]