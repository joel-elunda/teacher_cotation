"""teacher_cotation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('services/', TemplateView.as_view(template_name="services.html"), name='services'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('works/', TemplateView.as_view(template_name="works.html"), name='works'),
    
    path('teacher', include('teacher.urls')),
    path('student', include('student.urls')),
    path('cotation', include('cotation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
