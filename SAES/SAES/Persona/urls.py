from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.PersonaViewSet)

urlpatterns = [
	path('', include(router.urls)),
    # path('', views.index, name='index'),
    # path('store',views.store,name='store'),
    # path('login',views.CSRF_token,name='login'),
]