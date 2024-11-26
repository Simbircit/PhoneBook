from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact, name='PhoneBook'),
    path('contact_create/', views.contact_create, name='contact_create'),
    path('delete_contact/<contact_id>/', views.delete_contact, name='delete_contact'),
    path('update_favorite/<contact_id>/', views.update_favorite, name='update_favorite')
]
