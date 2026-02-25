from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),       # main app
    path('blog/', include('my_app.urls')),  # optional blog paths
    path('', include('orm_app.urls')),      # countries app
]