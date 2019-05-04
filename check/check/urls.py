"""check URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from CheckHos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^.*$',views.index),

#   批量处理审核
    url('^api$',views.api),
#   个人审核
    url(r'examine',views.examine),
#   插入融合的审核数据（用于训练）
    url(r'^insert$',views.insert),
#   比较检验大小
    url(r'cmp',views.cmp),
#   辅助诊断
    url(r'vtcheck',views.vtcheck)
]
