
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


#url patterns
urlpatterns = [
    url(r'^$', views.picture_list,name='picture_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.picture_list,name='picture_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.picture_detail,name='picture_detail'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)