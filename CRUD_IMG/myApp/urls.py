from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path("registration",views.registration,name='registration'),
    path("records",views.records,name='records'),
    path("deleteUser/<int:id>",views.deleteUser,name='deleteUser'),
    path("editUser/<int:id>",views.editUser,name='editUser'),
]
