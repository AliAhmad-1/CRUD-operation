from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [

    path("",views.UserAddStudent.as_view(), name="add"),

    path('delete/<int:id>',views.DeleteStudent.as_view(),name='delete'),

    path('update/<int:id>',views.UpdateStudent.as_view(),name='update'),

]
