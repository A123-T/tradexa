from django.urls import path
from testapp import views

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('',views.abhay,name = 'abhay'),
    path('post/',views.post_print,name = 'post_print'),
    path('update_post/',views.update_post,name = 'modify_post'),
    path('modify_post/<int:id1>',views.modify_post,name = 'modify'),
    path('alogin/',views.user_login,name= 'user_login'),
    path('user_logout/',views.user_logout,name = 'logout'),
    path('create/',views.create_post,name = 'create'),
]
