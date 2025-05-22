from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Dog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    picture = models.ImageField(upload_to='dogs/')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Cat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='cats_pictures/')
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class DogFoodRoutine(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, default=1)
    dog_name = models.CharField(max_length=100)
    sunday_morning = models.CharField(max_length=255)
    sunday_evening = models.CharField(max_length=255)
    monday_morning = models.CharField(max_length=255)
    monday_evening = models.CharField(max_length=255)
    tuesday_morning = models.CharField(max_length=255)
    tuesday_evening = models.CharField(max_length=255)
    wednesday_morning = models.CharField(max_length=255)
    wednesday_evening = models.CharField(max_length=255)
    thursday_morning = models.CharField(max_length=255)
    thursday_evening = models.CharField(max_length=255)
    friday_morning = models.CharField(max_length=255)
    friday_evening = models.CharField(max_length=255)
    saturday_morning = models.CharField(max_length=255)
    saturday_evening = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dog_name}'s Food Routine"
    


class DogHealthRoutine(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, default=1)
    dog_name = models.CharField(max_length=100)
    date1 = models.CharField(max_length=255)
    health_check1 = models.CharField(max_length=255)
    vaccination1 = models.CharField(max_length=255)
    date2 = models.CharField(max_length=255)
    health_check2 = models.CharField(max_length=255)
    vaccination2 = models.CharField(max_length=255)
    date3 = models.CharField(max_length=255)
    health_check3 = models.CharField(max_length=255)
    vaccination3 = models.CharField(max_length=255)
    date4 = models.CharField(max_length=255)
    health_check4 = models.CharField(max_length=255)
    vaccination4 = models.CharField(max_length=255)
    date5 = models.CharField(max_length=255)
    health_check5 = models.CharField(max_length=255)
    vaccination5 = models.CharField(max_length=255)
    date6 = models.CharField(max_length=255)
    health_check6 = models.CharField(max_length=255)
    vaccination6 = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.dog_name}'s Health Routine"
    

class DogGroomingRoutine(models.Model):
        
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, default=1)
    dog_name = models.CharField(max_length=100)

    date01 = models.DateField(blank=True, null=True)
    grooming01 = models.CharField(max_length=255, blank=True, null=True)
        
    date02 = models.DateField(blank=True, null=True)
    grooming02 = models.CharField(max_length=255, blank=True, null=True)

    date03 = models.DateField(blank=True, null=True)
    grooming03 = models.CharField(max_length=255, blank=True, null=True)

    date04 = models.DateField(blank=True, null=True)
    grooming04 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.dog_name}'s Grooming Routine"
    

class CatFoodRoutine(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, default=1)
    cat_name = models.CharField(max_length=100)
    sunday_morning1 = models.CharField(max_length=255)
    sunday_evening1 = models.CharField(max_length=255)
    monday_morning1 = models.CharField(max_length=255)
    monday_evening1 = models.CharField(max_length=255)
    tuesday_morning1 = models.CharField(max_length=255)
    tuesday_evening1 = models.CharField(max_length=255)
    wednesday_morning1 = models.CharField(max_length=255)
    wednesday_evening1 = models.CharField(max_length=255)
    thursday_morning1 = models.CharField(max_length=255)
    thursday_evening1 = models.CharField(max_length=255)
    friday_morning1 = models.CharField(max_length=255)
    friday_evening1 = models.CharField(max_length=255)
    saturday_morning1 = models.CharField(max_length=255)
    saturday_evening1 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cat_name}'s Food Routine"



class CatHealthRoutine(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, default=1)
    cat_name = models.CharField(max_length=100)
    date11 = models.CharField(max_length=255)
    health_check11 = models.CharField(max_length=255)
    vaccination11 = models.CharField(max_length=255)
    date22 = models.CharField(max_length=255)
    health_check22 = models.CharField(max_length=255)
    vaccination22 = models.CharField(max_length=255)
    date33 = models.CharField(max_length=255)
    health_check33 = models.CharField(max_length=255)
    vaccination33 = models.CharField(max_length=255)
    date44 = models.CharField(max_length=255)
    health_check44 = models.CharField(max_length=255)
    vaccination44 = models.CharField(max_length=255)
    date55 = models.CharField(max_length=255)
    health_check55 = models.CharField(max_length=255)
    vaccination55 = models.CharField(max_length=255)
    date66 = models.CharField(max_length=255)
    health_check66 = models.CharField(max_length=255)
    vaccination66 = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.cat_name}'s Health Routine"
    


class CatGroomingRoutine(models.Model):
        
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, default=1)
    cat_name = models.CharField(max_length=100)

    date101 = models.DateField(blank=True, null=True)
    grooming101 = models.CharField(max_length=255, blank=True, null=True)
        
    date102 = models.DateField(blank=True, null=True)
    grooming102 = models.CharField(max_length=255, blank=True, null=True)

    date103 = models.DateField(blank=True, null=True)
    grooming103 = models.CharField(max_length=255, blank=True, null=True)

    date104 = models.DateField(blank=True, null=True)
    grooming104 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.cat_name}'s Grooming Routine"
    


class GroomingBooking(models.Model):
    pet_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    address = models.TextField()

    def __str__(self):
        return f"{self.pet_name} - {self.date} at {self.time}"
