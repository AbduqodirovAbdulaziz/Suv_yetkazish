from django.contrib import admin
from django.urls import path,include
from mainApp.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('mijoz',MijozModelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('suvlar/',SuvlarApiView.as_view()),
    path('buyurtma/',BuyurtmaApiView.as_view()),
    path('haydovchilar/',HaydovchilarApiView.as_view()),
    path('adminlar/',AdminlarApiView.as_view()),
    path('haydovchilar/<int:pk>',HaydovchiApiView.as_view()),
    path('adminlar/<int:pk>',AdminApiViewSet.as_view()),
]
