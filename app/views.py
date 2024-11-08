from django.shortcuts import render,redirect
from django.contrib.auth import login 
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Pet,Petsitter,Service
# Create your views here.

def enter_service(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        add=request.POST.get('add')
        number=request.POST.get('num')
        
        service=Service(name=name,address=add,number=number)
        service.save()
        return redirect('home')
    return render(request,'app/enter_service.html')

def find_service(request):
    
    services=Service.objects.all()
    return render(request,'app/find_service.html',{'services':services})
    
 
    return render(request,'app/find_service.html')
def home(request):
    return render(request,'app/homepage.html')

def page1(request):
    return render(request,'app/page1.html')

def page2(request):
    return render(request,'app/page2.html')

def page3(request):
    return render(request,'app/page3.html') 

def page4(request):
    return render(request,'app/page4.html') 

def page5(request):
    return render(request,'app/page5.html')

def sell_pet(request):
    if request.method=='POST':
        name=request.POST.get('name')
        type=request.POST.get('type')
        breed=request.POST.get('breed')
        age=request.POST.get('age')
        health=request.POST.get('health')
        price=request.POST.get('price')
        owner_name=request.POST.get('owner_name')
        place=request.POST.get('place')
        number=request.POST.get('num')
        image=request.FILES.get('image')
        
        pet=Pet(name=name,pet_type=type,breed=breed,age=age,health=health,price=price,image=image,owner_name=owner_name,place=place,c_number=number)
        pet.save()
        return redirect('home')
    return render(request,'app/sell_your_pet.html') 

def buy_pet(request):
    pets=Pet.objects.all()
    return render(request,'app/buy_pet.html',{'pets':pets}) 

def become_pet_sitter(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('add')
        contact=request.POST.get('con')
        start_date=request.POST.get('from')
        end_date=request.POST.get('end')
        status=request.POST.get('status') 
        
        sitter=Petsitter(name=name,age=age,address=address,contact=contact,start_date=start_date,end_date=end_date,status=status)
        sitter.save()
        return redirect('home')
    return render(request,'app/become_a_pet_sitter.html')

def find_pet_sitter(request):
    from_date=request.GET.get('from')
    end_date=request.GET.get('end')
    
    if from_date and end_date:
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        
        sitters=Petsitter.objects.filter(start_date__lte=from_date,end_date__gte=end_date)
    else:
        sitters=Petsitter.objects.all()
    return render(request,'app/Find_Pit_Sitter.html',{'sitters':sitters})


def food_schedule(request):
    return render(request,'app/food_schedule.html') 

def training_tutorial(request):
    return render(request,'app/training_tutorial.html') 

def weight(request):
    return render(request,'app/weight.html') 

def vaccination(request):
    return render(request,'app/vacination_track.html')



    

def find_docter(request):
    if request.method == 'POST':
        location = request.POST.get('location')

            # Get latitude and longitude from the location using Nominatim
        geocode_url = f'https://nominatim.openstreetmap.org/search?format=json&q={location}'
        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()

        if geocode_data:
            lat = float(geocode_data[0]['lat'])
            lng = float(geocode_data[0]['lon'])

                # Find nearby pet hospitals using Overpass API
            overpass_url = (
                "http://overpass-api.de/api/interpreter?data="
                    f"[out:json];(node[\"amenity\"=\"veterinary\"]({lat - 0.009},{lng - 0.009},{lat + 0.002},{lng + 0.002}););out;"
                )
            nearby_response = requests.get(overpass_url)
            nearby_data = nearby_response.json()

            hospitals = nearby_data.get('elements', [])
            return render(request, 'app/Find_docter_nearby.html', {'hospitals': hospitals})

        else:
                # Handle case where geocoding fails
            return render(request, 'app/Find_docter_nearby.html', {'error': 'Location not found. Please try again.'})
 

    return render(request, 'app/Find_docter_nearby.html')


    

def register(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        
        if name and password and email:
            user=User.objects.create_user(username=name,password=password,email=email)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            return render(request,'app/signup.html')
    return render(request,'app/signup.html')
