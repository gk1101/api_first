from django.urls import path, include
from . import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('language', views.LanguageView)
# router basically registers the end points of the api
# so here, our endpoint is 'language'

urlpatterns = [
    #path('', include('language.urls'))
    path('', include(router.urls))

]
