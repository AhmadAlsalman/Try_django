from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.db.models.base import Model

# Register your models here.
from .models import Recipe, RecipeIngredient

#to register the model in admin
admin.site.register(RecipeIngredient)


#to show the RecipeIngredient in a better way
class RecipeIngredientInline(admin.StackedInline):
    model=RecipeIngredient
    extra=0 #to see few fields in the page 
    #fields=['name','quantity','unit','directions'] #if i want to limit the fields



class RecipeAdmin(admin.ModelAdmin):
    inlines=[RecipeIngredientInline]
    list_display=['name','user']
    readonly_fields=['timestamp','updated'] #so we cant change this fields
    raw_id_fields=['user'] #to show the user as id in admin page


admin.site.register(Recipe,RecipeAdmin)

