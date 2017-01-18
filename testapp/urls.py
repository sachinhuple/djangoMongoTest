from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'home',views.home, name='home'),
    url(r'save/', views.save, name='save'),
    url(r'savedetail/', views.detailform, name='detailform')
]