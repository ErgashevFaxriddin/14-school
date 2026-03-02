from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orm_app.urls')),     # 👈 ROOT delegation
    path('blog/', include('my_app.urls')),
]