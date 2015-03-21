from django.conf.urls import url,patterns

from dictionary import views

urlpatterns = patterns('',

    url(r'^$', views.search),
   ##  url(r'^result/$', views.result),
    url(r'^results/$',views.results),
    url(r'^results/dictionary/search/$',views.search),
)
