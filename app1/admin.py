from django.contrib import admin
from . models import Dog
from . models import Cat
from .models import DogHealthRoutine
from .models import DogFoodRoutine
from .models import DogGroomingRoutine
from .models import CatHealthRoutine
from .models import CatFoodRoutine
from .models import CatGroomingRoutine

# Register your models here.

class dogadmin(admin.ModelAdmin):
    list_display = ('name','email','breed','age','picture','password')

class catadmin(admin.ModelAdmin):
    list_display = ('name','email','breed','age','picture','password')


class DogFoodRoutineAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'sunday_morning', 'sunday_evening', 
                    'monday_morning', 'monday_evening', 'tuesday_morning', 
                    'tuesday_evening', 'wednesday_morning', 'wednesday_evening', 
                    'thursday_morning', 'thursday_evening', 'friday_morning', 
                    'friday_evening', 'saturday_morning', 'saturday_evening')

    search_fields = ('dog_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('dog_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('dog_name',)
        }),
        ('Weekly Routine', {
            'fields': (
                'sunday_morning', 'sunday_evening',
                'monday_morning', 'monday_evening',
                'tuesday_morning', 'tuesday_evening',
                'wednesday_morning', 'wednesday_evening',
                'thursday_morning', 'thursday_evening',
                'friday_morning', 'friday_evening',
                'saturday_morning', 'saturday_evening',
            )
        }),
    )

# Register the DogFoodRoutine model with custom admin options

class DogHealthRoutineAdmin(admin.ModelAdmin):
    list_display = ('dog_name','date1', 'health_check1', 'vaccination1',
                    'date2', 'health_check2', 'vaccination2',
                    'date3', 'health_check3', 'vaccination3',
                    'date4', 'health_check4', 'vaccination4',
                    'date5', 'health_check5', 'vaccination5',
                    'date6', 'health_check6', 'vaccination6')

    search_fields = ('dog_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('dog_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('dog_name',)
        }),
        ('Monthly Routine', {
            'fields': ('date1', 'health_check1', 'vaccination1',
                    'date2', 'health_check2', 'vaccination2',
                    'date3', 'health_check3', 'vaccination3',
                    'date4', 'health_check4', 'vaccination4',
                    'date5', 'health_check5', 'vaccination5',
                    'date6', 'health_check6', 'vaccination6',
            )
        }),
    )


class DogGroomingRoutineAdmin(admin.ModelAdmin):
    list_display = ('dog_name','date01', 'grooming01',
                    'date02', 'grooming02',
                    'date03', 'grooming03',
                    'date04', 'grooming04')

    search_fields = ('dog_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('dog_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('dog_name',)
        }),
        ('Monthly Routine', {
            'fields': ('date01', 'grooming01',
                    'date02', 'grooming02',
                    'date03', 'grooming03',
                    'date04', 'grooming04'
            )
        }),
    )


class CatFoodRoutineAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'sunday_morning1', 'sunday_evening1', 
                    'monday_morning1', 'monday_evening1', 'tuesday_morning1', 
                    'tuesday_evening1', 'wednesday_morning1', 'wednesday_evening1', 
                    'thursday_morning1', 'thursday_evening1', 'friday_morning1', 
                    'friday_evening1', 'saturday_morning1', 'saturday_evening1')

    search_fields = ('cat_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('cat_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('cat_name',)
        }),
        ('Weekly Routine', {
            'fields': (
                'sunday_morning1', 'sunday_evening1', 
                    'monday_morning1', 'monday_evening1', 'tuesday_morning1', 
                    'tuesday_evening1', 'wednesday_morning1', 'wednesday_evening1', 
                    'thursday_morning1', 'thursday_evening1', 'friday_morning1', 
                    'friday_evening1', 'saturday_morning1', 'saturday_evening1'
            )
        }),
    )


class CatHealthRoutineAdmin(admin.ModelAdmin):
    list_display = ('cat_name','date11', 'health_check11', 'vaccination11',
                    'date22', 'health_check22', 'vaccination22',
                    'date33', 'health_check33', 'vaccination33',
                    'date44', 'health_check44', 'vaccination44',
                    'date55', 'health_check55', 'vaccination55',
                    'date66', 'health_check66', 'vaccination66')

    search_fields = ('cat_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('cat_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('cat_name',)
        }),
        ('Monthly Routine', {
            'fields': ('date11', 'health_check11', 'vaccination11',
                    'date22', 'health_check22', 'vaccination22',
                    'date33', 'health_check33', 'vaccination33',
                    'date44', 'health_check44', 'vaccination44',
                    'date55', 'health_check55', 'vaccination55',
                    'date66', 'health_check66', 'vaccination66',
            )
        }),
    )


class CatGroomingRoutineAdmin(admin.ModelAdmin):
    list_display = ('cat_name','date101', 'grooming101',
                    'date102', 'grooming102',
                    'date103', 'grooming103',
                    'date104', 'grooming104')

    search_fields = ('cat_name',)

    # Optionally, add filters to help in searching the dog food routines
    list_filter = ('cat_name',)

    # Customize form for easier input
    fieldsets = (
        (None, {
            'fields': ('cat_name',)
        }),
        ('Monthly Routine', {
            'fields': ('date101', 'grooming101',
                    'date102', 'grooming102',
                    'date103', 'grooming103',
                    'date104', 'grooming104'
            )
        }),
    )



admin.site.register(Dog,dogadmin)
admin.site.register(Cat,catadmin)
admin.site.register(DogFoodRoutine, DogFoodRoutineAdmin)
admin.site.register(DogHealthRoutine, DogHealthRoutineAdmin)
admin.site.register(DogGroomingRoutine, DogGroomingRoutineAdmin)
admin.site.register(CatFoodRoutine, CatFoodRoutineAdmin)
admin.site.register(CatHealthRoutine, CatHealthRoutineAdmin)
admin.site.register(CatGroomingRoutine, CatGroomingRoutineAdmin)