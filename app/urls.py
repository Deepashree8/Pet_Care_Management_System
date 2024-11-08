from django.urls import path
from app import views 

app_name = 'app'

urlpatterns = [
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
    path('page3/',views.page3,name='page3'),
    path('page4/',views.page4,name='page4'),
    path('page5/',views.page5,name='page5'),
    path('sell_your_pet/',views.sell_pet,name='sell_pet'),
    path('buy_pet/',views.buy_pet,name='buy_pet'),
    path('become_pet_sitter/',views.become_pet_sitter,name='be_pet_sit'),
    path('find_pet_sitter/',views.find_pet_sitter,name='Find_Pet_Sit'),
    path('food_schedule/',views.food_schedule,name='food_schedule'),
    path('training_tutorial/',views.training_tutorial,name='training_tutorial'),
    path('weight/',views.weight,name='weight'),
    path('vaccination/',views.vaccination,name='vaccination'),
    path('find_docter/',views.find_docter,name='Find_docter'),
    path('signup/',views.register,name='signup'),
    path('sell/',views.sell_pet,name='sell'),
    path('enter_service/',views.enter_service,name='enter_service'),
    path('find_service/',views.find_service,name='find_service'),

]
