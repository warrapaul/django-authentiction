
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import AdminSite



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('landingPage.urls')),

]

admin.site.site_header = "SASAKONNECT Admin Panel"
admin.site.site_title = "SASAKONNECT"
admin.site.index_title = "Welcome to SASAKONNECT"

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
