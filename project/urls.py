from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    path(settings.ADMIN_PATH + '/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    url(r'mdeditor/', include('mdeditor.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
