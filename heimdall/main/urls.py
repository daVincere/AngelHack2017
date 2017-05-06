from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
	# url(r'^', views.api_root,),
	url(r'^traffic/$', views.TrafficView.as_view(), name='traffic-list',),
	url(r'^traffic/(?P<pk>[0-9]+)/$', views.TrafficDetailView.as_view(), name='traffic-detail'),
	url(r'^location/$', views.LocationView.as_view(), name='location-list'),
	url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail'),
])


urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 