from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from WiaGo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'node', views.NodeViewSet)
router.register(r'notif', views.NotifViewSet)
router.register(r'state', views.StateViewSet)




urlpatterns = [
    path('c_node/', views.create_node),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
