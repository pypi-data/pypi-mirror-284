from django.urls import path
from rest_framework.routers import SimpleRouter

from new_plugin import views


router = SimpleRouter()

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='new_plugin')

]

urlpatterns += router.urls