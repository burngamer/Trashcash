
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
