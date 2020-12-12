from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('', index, name='home'),

]
