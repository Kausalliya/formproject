from .import views
from django.urls import path

urlpatterns = [
    # path('',views.add,name="add"),
    path('',views.addemp,name='addemp'),
    path('show/',views.show,name="show"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),

]
