from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('foro.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('universities.urls'))

]

