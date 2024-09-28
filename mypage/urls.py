from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define the path to different webpages. Represent the urls to different pages

urlpatterns = [
    path("", views.home, name="home")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path("<str:name>", views.idk, name="idk"),