from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('todo',views.TodoView)
router.register('calender',views.CalnderView)


urlpatterns = [
    path('',include(router.urls))
]