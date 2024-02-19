from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include("tasks.urls")),
    path('newyear/', include("newyear.urls")),
    path('hello/', include("hello.urls"))
]
