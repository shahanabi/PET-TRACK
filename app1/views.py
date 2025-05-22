from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def register_dog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        picture = request.FILES.get('picture')
        password = request.POST.get('password')

        Dog.objects.create(
            name=name,
            email=email,
            breed=breed,
            age=age,
            picture=picture,
            password=password  # Note: Storing raw password like this is not safe for real apps
        )

        return redirect('homepage')

    return render(request, 'register_dog.html')


def register_cat(request):
    if request.method == "POST":
        # Get data from the form
        email = request.POST['email']
        name = request.POST['name']
        breed = request.POST['breed']
        age = request.POST['age']
        picture = request.FILES['picture']
        password = request.POST['password']

        # Save the cat in the database
        cat = Cat(
            email=email,
            name=name,
            breed=breed,
            age=age,
            picture=picture,
            password=password
        )
        cat.save()

        # After registration, redirect to a success page or the login page
        return redirect('homepage')

    return render(request, 'register_cat.html')

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Check if the email and password match for a Dog
    dogdetails = Dog.objects.filter(email=email, password=password).first()
    if dogdetails:  # If dogdetails is not None, it means a matching dog was found
        request.session['did'] = dogdetails.id
        request.session['dname'] = dogdetails.name
        request.session['email'] = email
        request.session['duser'] = 'duser'

        return render(request, 'homepage.html')

    # Check if the email and password match for a Cat
    catdetails = Cat.objects.filter(email=email, password=password).first()
    if catdetails:  # If catdetails is not None, it means a matching cat was found
        request.session['cid'] = catdetails.id
        request.session['cname'] = catdetails.name
        request.session['cmail'] = email
        request.session['cuser'] = 'cuser'  # Changed 'duser' to 'cuser' for clarity

        return render(request, 'homepage.html')

    # If no match is found for either Dog or Cat
    return render(request, 'login.html', {'status': 'Invalid email or password'})

def logout(request):
    session_key = list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect(homepage)

def dog_routine(request):
    return render(request, 'dog_routine.html')



def dog_feeding_schedule(request):
    dog_id = request.session.get('did')
    try:
        routine = DogFoodRoutine.objects.get(dog_id=dog_id)
    except DogFoodRoutine.DoesNotExist:
        routine = None

    return render(request, 'dog_feeding_schedule.html', {'routine': routine})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Dog, DogFoodRoutine

def dog_food_routine(request, id):
    # Get the dog instance or return 404
    dog = get_object_or_404(Dog, id=id)
    
    # Get existing routine or initialize new one
    routine, created = DogFoodRoutine.objects.get_or_create(dog=dog)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.sunday_morning = request.POST.get("sunday_morning", "")
        routine.sunday_evening = request.POST.get("sunday_evening", "")
        routine.monday_morning = request.POST.get("monday_morning", "")
        routine.monday_evening = request.POST.get("monday_evening", "")
        routine.tuesday_morning = request.POST.get("tuesday_morning", "")
        routine.tuesday_evening = request.POST.get("tuesday_evening", "")
        routine.wednesday_morning = request.POST.get("wednesday_morning", "")
        routine.wednesday_evening = request.POST.get("wednesday_evening", "")
        routine.thursday_morning = request.POST.get("thursday_morning", "")
        routine.thursday_evening = request.POST.get("thursday_evening", "")
        routine.friday_morning = request.POST.get("friday_morning", "")
        routine.friday_evening = request.POST.get("friday_evening", "")
        routine.saturday_morning = request.POST.get("saturday_morning", "")
        routine.saturday_evening = request.POST.get("saturday_evening", "")
        routine.save()
        return redirect('dog_food_view', id=routine.id)

    return render(request, 'dog_food_routine.html', {
        'dog': dog,
        'routine': routine,
        'did': id
    })

def dog_food_view(request, id):
    routine = get_object_or_404(DogFoodRoutine, id=id)
    return render(request, 'dog_food_view.html', {
        'routine': routine,
        'dog_id': routine.dog.id  # Now properly references the Dog's ID
    })
       

def dog_food_edit(request, id):
    routine = get_object_or_404(DogFoodRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.sunday_morning = request.POST.get("sunday_morning", "")
        routine.sunday_evening = request.POST.get("sunday_evening", "")
        routine.monday_morning = request.POST.get("monday_morning", "")
        routine.monday_evening = request.POST.get("monday_evening", "")
        routine.tuesday_morning = request.POST.get("tuesday_morning", "")
        routine.tuesday_evening = request.POST.get("tuesday_evening", "")
        routine.wednesday_morning = request.POST.get("wednesday_morning", "")
        routine.wednesday_evening = request.POST.get("wednesday_evening", "")
        routine.thursday_morning = request.POST.get("thursday_morning", "")
        routine.thursday_evening = request.POST.get("thursday_evening", "")
        routine.friday_morning = request.POST.get("friday_morning", "")
        routine.friday_evening = request.POST.get("friday_evening", "")
        routine.saturday_morning = request.POST.get("saturday_morning", "")
        routine.saturday_evening = request.POST.get("saturday_evening", "")
        routine.save()
        
        return redirect('dog_food_view', id=routine.id)

    return render(request, 'dog_food_edit.html', {
        'routine': routine,
        'dog_id': routine.dog.id
    })



def dog_health_schedule(request):
    dog_id = request.session.get('did')
    try:
        routine = DogHealthRoutine.objects.get(dog_id=dog_id)
    except DogHealthRoutine.DoesNotExist:
        routine = None

    return render(request, 'dog_health_schedule.html', {'routine': routine})


def dog_health_routine(request, id):
    # Get the dog instance or return 404
    dog = get_object_or_404(Dog, id=id)
    
    # Get existing routine or initialize new one
    routine, created = DogHealthRoutine.objects.get_or_create(dog=dog)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.date1 = request.POST.get("date1", "")
        routine.health_check1 = request.POST.get("health_check1", "")
        routine.vaccination1 = request.POST.get("vaccination1", "")
        routine.date2 = request.POST.get("date2", "")
        routine.health_check2 = request.POST.get("health_check2", "")
        routine.vaccination2 = request.POST.get("vaccination2", "")
        routine.date3 = request.POST.get("date3", "")
        routine.health_check3 = request.POST.get("health_check3", "")
        routine.vaccination3 = request.POST.get("vaccination3", "")
        routine.date4 = request.POST.get("date4", "")
        routine.health_check4 = request.POST.get("health_check4", "")
        routine.vaccination4 = request.POST.get("vaccination4", "")
        routine.date5 = request.POST.get("date5", "")
        routine.health_check5 = request.POST.get("health_check5", "")
        routine.vaccination5 = request.POST.get("vaccination5", "")
        routine.date6 = request.POST.get("date6", "")
        routine.health_check6 = request.POST.get("health_check6", "")
        routine.vaccination6 = request.POST.get("vaccination6", "")
        routine.save()
        return redirect('dog_health_view', id=routine.id)

    return render(request, 'dog_health_routine.html', {
        'dog': dog,
        'routine': routine,
        'did': id
    })

def dog_health_view(request, id):
    routine = get_object_or_404(DogHealthRoutine, id=id)
    return render(request, 'dog_health_view.html', {
        'routine': routine,
        'dog_id': routine.dog.id  # Now properly references the Dog's ID
    })

def dog_health_edit(request, id):
    routine = get_object_or_404(DogHealthRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.date1 = request.POST.get("date1", "")
        routine.health_check1 = request.POST.get("health_check1", "")
        routine.vaccination1 = request.POST.get("vaccination1", "")
        routine.date2 = request.POST.get("date2", "")
        routine.health_check2 = request.POST.get("health_check2", "")
        routine.vaccination2 = request.POST.get("vaccination2", "")
        routine.date3 = request.POST.get("date3", "")
        routine.health_check3 = request.POST.get("health_check3", "")
        routine.vaccination3 = request.POST.get("vaccination3", "")
        routine.date4 = request.POST.get("date4", "")
        routine.health_check4 = request.POST.get("health_check4", "")
        routine.vaccination4 = request.POST.get("vaccination4", "")
        routine.date5 = request.POST.get("date5", "")
        routine.health_check5 = request.POST.get("health_check5", "")
        routine.vaccination5 = request.POST.get("vaccination5", "")
        routine.date6 = request.POST.get("date6", "")
        routine.health_check6 = request.POST.get("health_check6", "")
        routine.vaccination6 = request.POST.get("vaccination6", "")
        routine.save()
        
        return redirect('dog_health_view', id=routine.id)

    return render(request, 'dog_health_edit.html', {
        'routine': routine,
        'dog_id': routine.dog.id
    })


def dog_grooming_schedule(request):
    dog_id = request.session.get('did')
    try:
        routine = DogGroomingRoutine.objects.get(dog_id=dog_id)
    except DogGroomingRoutine.DoesNotExist:
        routine = None

    return render(request, 'dog_grooming_schedule.html', {'routine': routine})


def dog_grooming_routine(request, id):
    # Get the dog instance or return 404
    dog = get_object_or_404(Dog, id=id)
    
    # Get existing routine or initialize new one
    routine, created = DogGroomingRoutine.objects.get_or_create(dog=dog)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.date01 = request.POST.get("date01", "")
        routine.grooming01 = request.POST.get("grooming01", "")
        routine.date02 = request.POST.get("date02", "")
        routine.grooming02 = request.POST.get("grooming02", "")
        routine.date03 = request.POST.get("date03", "")
        routine.grooming03 = request.POST.get("grooming03", "")
        routine.date04 = request.POST.get("date04", "")
        routine.grooming04 = request.POST.get("grooming04", "")
        routine.save()
        return redirect('dog_grooming_view', id=routine.id)

    return render(request, 'dog_grooming_routine.html', {
        'dog': dog,
        'routine': routine,
        'did': id
    })

def dog_grooming_view(request, id):
    routine = get_object_or_404(DogGroomingRoutine, id=id)
    return render(request, 'dog_grooming_view.html', {
        'routine': routine,
        'dog_id': routine.dog.id  # Now properly references the Dog's ID
    })

def dog_grooming_edit(request, id):
    routine = get_object_or_404(DogGroomingRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.date01 = request.POST.get("date01", "")
        routine.grooming01 = request.POST.get("grooming01", "")
        routine.date02 = request.POST.get("date02", "")
        routine.grooming02 = request.POST.get("grooming02", "")
        routine.date03 = request.POST.get("date03", "")
        routine.grooming03 = request.POST.get("grooming03", "")
        routine.date04 = request.POST.get("date04", "")
        routine.grooming04 = request.POST.get("grooming04", "")
        routine.save()
        
        return redirect('dog_grooming_view', id=routine.id)

    return render(request, 'dog_grooming_edit.html', {
        'routine': routine,
        'dog_id': routine.dog.id
    })


def cat_routine(request):
    return render(request, 'cat_routine.html')


def cat_food_schedule(request):
    cat_id = request.session.get('cid')
    try:
        routine = CatFoodRoutine.objects.get(cat_id=cat_id)
    except CatFoodRoutine.DoesNotExist:
        routine = None

    return render(request, 'cat_food_schedule.html', {'routine': routine})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat, CatFoodRoutine

def cat_food_routine(request, id):
    cat = get_object_or_404(Cat, id=id)
    
    # Get existing routine or initialize new one
    routine, created = CatFoodRoutine.objects.get_or_create(cat=cat)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.sunday_morning1 = request.POST.get("sunday_morning1", "")
        routine.sunday_evening1 = request.POST.get("sunday_evening1", "")
        routine.monday_morning1 = request.POST.get("monday_morning1", "")
        routine.monday_evening1 = request.POST.get("monday_evening1", "")
        routine.tuesday_morning1 = request.POST.get("tuesday_morning1", "")
        routine.tuesday_evening1 = request.POST.get("tuesday_evening1", "")
        routine.wednesday_morning1 = request.POST.get("wednesday_morning1", "")
        routine.wednesday_evening1 = request.POST.get("wednesday_evening1", "")
        routine.thursday_morning1 = request.POST.get("thursday_morning1", "")
        routine.thursday_evening1 = request.POST.get("thursday_evening1", "")
        routine.friday_morning1 = request.POST.get("friday_morning1", "")
        routine.friday_evening1 = request.POST.get("friday_evening1", "")
        routine.saturday_morning1 = request.POST.get("saturday_morning1", "")
        routine.saturday_evening1 = request.POST.get("saturday_evening1", "")
        routine.save()
        return redirect('cat_food_view', id=routine.id)

    return render(request, 'cat_food_routine.html', {
        'cat': cat,
        'routine': routine,
        'cid': id
    })

def cat_food_view(request, id):
    routine = get_object_or_404(CatFoodRoutine, id=id)
    return render(request, 'cat_food_view.html', {
        'routine': routine,
        'cat_id': routine.cat.id 
    })
       

def cat_food_edit(request, id):
    routine = get_object_or_404(CatFoodRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.sunday_morning1 = request.POST.get("sunday_morning1", "")
        routine.sunday_evening1 = request.POST.get("sunday_evening1", "")
        routine.monday_morning1 = request.POST.get("monday_morning1", "")
        routine.monday_evening1 = request.POST.get("monday_evening1", "")
        routine.tuesday_morning1 = request.POST.get("tuesday_morning1", "")
        routine.tuesday_evening1 = request.POST.get("tuesday_evening1", "")
        routine.wednesday_morning1 = request.POST.get("wednesday_morning1", "")
        routine.wednesday_evening1 = request.POST.get("wednesday_evening1", "")
        routine.thursday_morning1 = request.POST.get("thursday_morning1", "")
        routine.thursday_evening1 = request.POST.get("thursday_evening1", "")
        routine.friday_morning1 = request.POST.get("friday_morning1", "")
        routine.friday_evening1 = request.POST.get("friday_evening1", "")
        routine.saturday_morning1 = request.POST.get("saturday_morning1", "")
        routine.saturday_evening1 = request.POST.get("saturday_evening1", "")
        routine.save()
        
        return redirect('cat_food_view', id=routine.id)

    return render(request, 'cat_food_edit.html', {
        'routine': routine,
        'cat_id': routine.cat.id
    })



def cat_health_schedule(request):
    cat_id = request.session.get('cid')
    try:
        routine = CatHealthRoutine.objects.get(cat_id=cat_id)
    except CatHealthRoutine.DoesNotExist:
        routine = None

    return render(request, 'cat_health_schedule.html', {'routine': routine})



def cat_health_routine(request, id):
    # Get the dog instance or return 404
    cat = get_object_or_404(Cat, id=id)
    
    # Get existing routine or initialize new one
    routine, created = CatHealthRoutine.objects.get_or_create(cat=cat)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.date11 = request.POST.get("date11", "")
        routine.health_check11 = request.POST.get("health_check11", "")
        routine.vaccination11 = request.POST.get("vaccination11", "")
        routine.date22 = request.POST.get("date22", "")
        routine.health_check22 = request.POST.get("health_check22", "")
        routine.vaccination22 = request.POST.get("vaccination22", "")
        routine.date33 = request.POST.get("date33", "")
        routine.health_check33 = request.POST.get("health_check33", "")
        routine.vaccination33 = request.POST.get("vaccination33", "")
        routine.date44 = request.POST.get("date44", "")
        routine.health_check44 = request.POST.get("health_check44", "")
        routine.vaccination44 = request.POST.get("vaccination44", "")
        routine.date55 = request.POST.get("date55", "")
        routine.health_check55 = request.POST.get("health_check55", "")
        routine.vaccination55 = request.POST.get("vaccination55", "")
        routine.date66 = request.POST.get("date66", "")
        routine.health_check66 = request.POST.get("health_check66", "")
        routine.vaccination66 = request.POST.get("vaccination66", "")
        routine.save()
        return redirect('cat_health_view', id=routine.id)

    return render(request, 'cat_health_routine.html', {
        'cat': cat,
        'routine': routine,
        'cid': id
    })

def cat_health_view(request, id):
    routine = get_object_or_404(CatHealthRoutine, id=id)
    return render(request, 'cat_health_view.html', {
        'routine': routine,
        'cat_id': routine.cat.id  # Now properly references the Dog's ID
    })

def cat_health_edit(request, id):
    routine = get_object_or_404(CatHealthRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.date11 = request.POST.get("date11", "")
        routine.health_check11 = request.POST.get("health_check11", "")
        routine.vaccination11 = request.POST.get("vaccination11", "")
        routine.date22 = request.POST.get("date22", "")
        routine.health_check22 = request.POST.get("health_check22", "")
        routine.vaccination22 = request.POST.get("vaccination22", "")
        routine.date33 = request.POST.get("date33", "")
        routine.health_check33 = request.POST.get("health_check33", "")
        routine.vaccination33 = request.POST.get("vaccination33", "")
        routine.date44 = request.POST.get("date44", "")
        routine.health_check44 = request.POST.get("health_check44", "")
        routine.vaccination44 = request.POST.get("vaccination44", "")
        routine.date55 = request.POST.get("date55", "")
        routine.health_check55 = request.POST.get("health_check55", "")
        routine.vaccination55 = request.POST.get("vaccination55", "")
        routine.date66 = request.POST.get("date66", "")
        routine.health_check66 = request.POST.get("health_check66", "")
        routine.vaccination66 = request.POST.get("vaccination66", "")
        routine.save()
        
        return redirect('cat_health_view', id=routine.id)

    return render(request, 'cat_health_edit.html', {
        'routine': routine,
        'cat_id': routine.cat.id
    })



def cat_grooming_schedule(request):
    cat_id = request.session.get('cid')
    try:
        routine = CatGroomingRoutine.objects.get(cat_id=cat_id)
    except CatGroomingRoutine.DoesNotExist:
        routine = None

    return render(request, 'cat_grooming_schedule.html', {'routine': routine})




def cat_grooming_routine(request, id):
    # Get the dog instance or return 404
    cat = get_object_or_404(Cat, id=id)
    
    # Get existing routine or initialize new one
    routine, created = CatGroomingRoutine.objects.get_or_create(cat=cat)
    
    if request.method == "POST":
        # Update all fields from POST data
        routine.date101 = request.POST.get("date101", "")
        routine.grooming101 = request.POST.get("grooming101", "")
        routine.date102 = request.POST.get("date102", "")
        routine.grooming102 = request.POST.get("grooming102", "")
        routine.date103 = request.POST.get("date103", "")
        routine.grooming103 = request.POST.get("grooming103", "")
        routine.date104 = request.POST.get("date104", "")
        routine.grooming104 = request.POST.get("grooming104", "")
        routine.save()
        return redirect('cat_grooming_view', id=routine.id)

    return render(request, 'cat_grooming_routine.html', {
        'cat': cat,
        'routine': routine,
        'cid': id
    })

def cat_grooming_view(request, id):
    routine = get_object_or_404(CatGroomingRoutine, id=id)
    return render(request, 'cat_grooming_view.html', {
        'routine': routine,
        'cat_id': routine.cat.id  
    })

def cat_grooming_edit(request, id):
    routine = get_object_or_404(CatGroomingRoutine, id=id)
    
    if request.method == "POST":
        # Update all fields from form data
        routine.date101 = request.POST.get("date101", "")
        routine.grooming101 = request.POST.get("grooming101", "")
        routine.date102 = request.POST.get("date102", "")
        routine.grooming102 = request.POST.get("grooming102", "")
        routine.date103 = request.POST.get("date103", "")
        routine.grooming103 = request.POST.get("grooming103", "")
        routine.date104 = request.POST.get("date104", "")
        routine.grooming104 = request.POST.get("grooming104", "")
        routine.save()
        
        return redirect('cat_grooming_view', id=routine.id)

    return render(request, 'cat_grooming_edit.html', {
        'routine': routine,
        'cat_id': routine.cat.id
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Dog

# Display dog profile
def dog_profile(request):
    try:
        dog_id = request.session['did']  # make sure 'did' is set during login/registration
        dog = Dog.objects.get(id=dog_id)
        return render(request, 'dog_profile.html', {'result': dog})
    except KeyError:
        return redirect('login')  # or show error page
    except Dog.DoesNotExist:
        return redirect('register')  # or handle missing dog profile gracefully


# Edit dog profile
def dog_profile_edit(request, id):
    dog = get_object_or_404(Dog, id=id)

    if request.method == 'POST':
        dog.name = request.POST.get('name')
        dog.email = request.POST.get('email')
        dog.breed = request.POST.get('breed')
        dog.age = request.POST.get('age')
        dog.password = request.POST.get('password')

        if 'picture' in request.FILES:
            dog.picture = request.FILES['picture']

        dog.save()
        return redirect('dog_profile')  # after saving, go back to profile page

    return render(request, 'dog_profile_edit.html', {'result': dog})



def cat_profile(request):
    try:
        cat_id = request.session['cid']  # make sure 'did' is set during login/registration
        cat = Cat.objects.get(id=cat_id)
        return render(request, 'cat_profile.html', {'result': cat})
    except KeyError:
        return redirect('login')  # or show error page
    except Cat.DoesNotExist:
        return redirect('register')  # or handle missing cat profile gracefully


# Edit cat profile
def cat_profile_edit(request, id):
    cat = get_object_or_404(Cat, id=id)

    if request.method == 'POST':
        cat.name = request.POST.get('name')
        cat.email = request.POST.get('email')
        cat.breed = request.POST.get('breed')
        cat.age = request.POST.get('age')
        cat.password = request.POST.get('password')

        if 'picture' in request.FILES:
            cat.picture = request.FILES['picture']

        cat.save()
        return redirect('cat_profile')  # after saving, go back to profile page

    return render(request, 'cat_profile_edit.html', {'result': cat})


from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import GroomingBooking

def book_grooming(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_grooming')
    else:
        form = BookingForm()

    bookings = GroomingBooking.objects.all().order_by('date', 'time')
    return render(request, 'booking.html', {'form': form, 'bookings': bookings})
