from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# main URL routing for the whole project
urlpatterns = [
    # admin panel – only for staff/superuser
    path('admin/', admin.site.urls),

    # default homepage showing list of games
    path('', include('games.urls')),

    # authentication routes (register / login / logout)
    path('accounts/', include('authapp.urls')),
]

# enable serving uploaded images during development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
