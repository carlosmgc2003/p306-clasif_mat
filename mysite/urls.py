from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from clasif_mat import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'signup'}, name='logout'),
    url(r'^$', views.lista_registros, name='home'),
    url(r'^registro/(?P<pk>[0-9]+)/$', views.detalle_registro, name='detalle_registro'),
    url(r'^registro/([0-9]+)/uploads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<name>[a-zA-Z0-9_]+)',views.vista_pdf),
    url(r'^registro/nuevo/$', views.registro_nuevo, name='nuevo_registro'),
    url(r'^uploads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<name>[a-zA-Z0-9_]+)',views.vista_pdf)
]
