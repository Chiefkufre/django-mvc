from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.

from .models import Recipe, RecipeIngredient



User = get_user_model()

admin.site.unregister(User)


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inline = [RecipeInline]
    list_display = ['username']


admin.site.register(User, UserAdmin)
# class RecipeIngredientInline(admin.TabularInline):
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    # radio_fields = ['user']
   



admin.site.register(Recipe, RecipeAdmin)


# admin.site.register(RecipeIngredient)



