from django.urls import path
from .views import submit_form, contacts

urlpatterns = [
    path('submit/',   submit_form),
    path('contacts/', contacts, name='contacts'),
]
