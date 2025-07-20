
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('core.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    
]
