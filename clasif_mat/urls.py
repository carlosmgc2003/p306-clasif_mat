from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.lista_registros),
    url(r'^registro/(?P<pk>[0-9]+)/$', views.detalle_registro, name='detalle_registro'),
    url(r'^registro/([0-9]+)/uploads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<name>[a-zA-Z0-9_]+)',views.vista_pdf),
    url(r'^registro/nuevo/$', views.registro_nuevo, name='registro_nuevo'),
    url(r'^uploads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<name>[a-zA-Z0-9_]+)',views.vista_pdf)
]

"""
    comienza con ^ otra vez, "el principio".
    post/ sólo significa que después del comienzo, la dirección URL debe contener la palabra post y /. Hasta ahora, bien.
    (?P<pk>[0-9]+) - esta parte es más complicada. Significa que Django llevará todo lo que coloques aquí y lo transferirá
     a una vista como una variable llamada pk. [0-9] también nos dice que sólo puede ser un número, no una letra (todo 
     debería estar entre 0 y 9). + significa que tiene que haber uno o más dígitos. Entonces algo como http://127.0.0.1:8000/post// 
     no es válido, pero http://127.0.0.1:8000/post/1234567890/ es perfectamente aceptable!
    / - entonces necesitamos / de nuevo
    $ - ¡"el final"!
    Eso significa que si entras en http://127.0.0.1:8000/post/5/ en tu navegador, Django entenderá que estás buscando una view denominada
     post_detail y transferirá la información de pk que es igual a 5 a esa view.
"""