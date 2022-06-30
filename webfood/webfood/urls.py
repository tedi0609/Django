from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pesanan/', include('pesanan.urls')),
    path('admin/', admin.site.urls),
]
