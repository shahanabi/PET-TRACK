from django.urls import path, include
from . import views


urlpatterns =[
     path('', views.homepage, name='homepage'),

     path('register_dog/', views.register_dog, name='register_dog'),

     path('register_cat/', views.register_cat, name='register_cat'),

     path('login/', views.login, name='login'),

     path('logout/', views.logout, name='logout'),

     path('dog_routine/', views.dog_routine, name='dog_routine'),

     path('dog_feeding_schedule/', views.dog_feeding_schedule, name='dog_feeding_schedule'),

    path('dog_food_routine/<int:id>/', views.dog_food_routine, name='dog_food_routine'),

    path('dog_food_view/<int:id>/', views.dog_food_view, name='dog_food_view'),

    path('dog_food_edit/<int:id>/', views.dog_food_edit, name='dog_food_edit'),

    path('dog_health_schedule/', views.dog_health_schedule, name='dog_health_schedule'),

    path('dog_health_routine/<int:id>/', views.dog_health_routine, name='dog_health_routine'),

    path('dog_health_view/<int:id>/', views.dog_health_view, name='dog_health_view'),

    path('dog_health_edit/<int:id>/', views.dog_health_edit, name='dog_health_edit'),

    path('dog_grooming_schedule/', views.dog_grooming_schedule, name='dog_grooming_schedule'),

    path('dog_grooming_routine/<int:id>/', views.dog_grooming_routine, name='dog_grooming_routine'),

    path('dog_grooming_view/<int:id>/', views.dog_grooming_view, name='dog_grooming_view'),

    path('dog_grooming_edit/<int:id>/', views.dog_grooming_edit, name='dog_grooming_edit'),
 
    path('cat_routine/', views.cat_routine, name='cat_routine'),

    path('cat_food_schedule/', views.cat_food_schedule, name='cat_food_schedule'),

    path('cat_food_routine/<int:id>/', views.cat_food_routine, name='cat_food_routine'),

    path('cat_food_view/<int:id>/', views.cat_food_view, name='cat_food_view'),

    path('cat_food_edit/<int:id>/', views.cat_food_edit, name='cat_food_edit'),

    path('cat_health_schedule/', views.cat_health_schedule, name='cat_health_schedule'),

    path('cat_health_routine/<int:id>/', views.cat_health_routine, name='cat_health_routine'),

    path('cat_health_view/<int:id>/', views.cat_health_view, name='cat_health_view'),

    path('cat_health_edit/<int:id>/', views.cat_health_edit, name='cat_health_edit'),

    path('cat_grooming_schedule/', views.cat_grooming_schedule, name='cat_grooming_schedule'),

    path('cat_grooming_routine/<int:id>/', views.cat_grooming_routine, name='cat_grooming_routine'),

    path('cat_grooming_view/<int:id>/', views.cat_grooming_view, name='cat_grooming_view'),

    path('cat_grooming_edit/<int:id>/', views.cat_grooming_edit, name='cat_grooming_edit'),

    path('dog_profile/', views.dog_profile, name='dog_profile'),

    path('dog_profile_edit/<int:id>/', views.dog_profile_edit, name='dog_profile_edit'),

    path('cat_profile/', views.cat_profile, name='cat_profile'),
    
    path('cat_profile_edit/<int:id>/', views.cat_profile_edit, name='cat_profile_edit'),

    path('book/', views.book_grooming, name='book_grooming'),

]