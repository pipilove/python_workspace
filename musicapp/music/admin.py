from django.contrib import admin

# Register your models here.
# from music.models import Publisher,Author,Book
from music.models import Login,Item1,Item2,Item2Tag,Hotmusic,User,Recmusic

admin.site.register(Login)
admin.site.register(User)
admin.site.register(Item1)
admin.site.register(Hotmusic)
admin.site.register(Recmusic)
admin.site.register(Item2)
admin.site.register(Item2Tag)