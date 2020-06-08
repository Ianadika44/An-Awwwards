from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.awards,name = 'main'),
    url(r'^profile/$', views.profile_info, name='profile_info'),
    url(r'^awards/$', views.awards, name='awards'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^ajax/awardletter/$', views.awardletter, name='awardletter'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)