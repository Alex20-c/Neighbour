from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static  import static


urlpatterns = [
    url('^$',views.index,name='index'),  
    url(r'^hood/(?P<location>\w+)',views.single_hood,name='single_hood'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 