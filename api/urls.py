from django.urls import path,include
from .views import StudentViewSet
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('student',StudentViewSet,basename='stu_api')
urlpatterns = [
# path('',include(router.urls)),
path('student/<int:student_id>/',views.student_api,name='student_api'),
path('student/',views.student_api,name='student_api')
]

