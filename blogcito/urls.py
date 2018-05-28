from django.conf.urls import patterns, include, url

from django.contrib import admin
import blog.views as views
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogcito.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^post_crea$', views.post_crea, name='post_crea'), #cuando es asi no lleva comillas ni el / ni blog
    url(r'^(?P<slug>[\w\-]+)/edita/$', views.post_edita, name='post_edita'),
)
