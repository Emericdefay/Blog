from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# Used for SSL Certificat at : https://www.httpcs.com/
# from .views import security_txt  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('mdeditor/', include('mdeditor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('comment/', include('comment.urls')),
    path('resume/', include('resume.urls')),
    path('contact/', include('contact.urls')),
    # Used for SSL Certificat at : https://www.httpcs.com/
    # path(".well-known/pki-validation/EC523B3318EF62A7C00C36E8629DF486.txt", security_txt),
]

# if settings.DEBUG:
if True:
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
