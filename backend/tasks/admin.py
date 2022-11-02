from django.contrib import admin

from .models import Task

# Register your models here.

# create a class for the admin-model integration
class TaskAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("title", "description", "completed", "created_at")


# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Task, TaskAdmin)