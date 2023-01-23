"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ninja import NinjaAPI
# from lexnetix.api import router as lex_router
from lexnetix.API.school_api import router as school_router
from lexnetix.API.headmaster_api import router as headmaster_router
from lexnetix.API.Info_api import router as info_router
from lexnetix.API.teacher_api import router as teacher_router
from lexnetix.API.student_api import router as student_router
from lexnetix.API.class_api import router as class_router


api = NinjaAPI()
api.add_router('', school_router)
api.add_router('', headmaster_router)
api.add_router('', info_router)
api.add_router('', teacher_router)
api.add_router('', student_router)
api.add_router('', class_router)
# api.add_router('', lex_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
