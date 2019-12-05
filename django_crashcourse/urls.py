from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Import setting for media upload
from django.conf import settings
from django.conf.urls.static import static

# Imports from Custom Apps views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^store/', include('books.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
