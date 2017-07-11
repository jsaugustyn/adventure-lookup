from django.contrib import admin
from .models import Adventure, Rating, System, Availability, Terrain
#from .models import User, Adventure, Rating, System, Availability, Terrain


# Register your models here.
#admin.site.register(User)
admin.site.register(Adventure)
admin.site.register(Rating)
admin.site.register(System)
admin.site.register(Availability)
admin.site.register(Terrain)