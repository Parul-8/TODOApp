from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('add-todo/',views.add_todo),
    path('delete-todo/<int:id>',views.delete),
    path('change-status/<int:id>/<str:status>',views.change_todo),
    path('logout/',views.signout),
    
    
]