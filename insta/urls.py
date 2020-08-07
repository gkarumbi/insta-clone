
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[

    url(r'', home_page),
    url(r'^profile/', user_profile),
    url(r'^uploads/'photo_upload)

    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)