from django.urls import path
from product import views

urlpatterns = [
     path('',views.abhinav,name = 'abhinav'),
     path('show/',views.show_data,name='show_data'),
     path('modify/<int:id>',views.modify123,name='modify2'),

]
