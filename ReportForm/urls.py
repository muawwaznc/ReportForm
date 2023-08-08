"""ReportForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ReportForm import views
from app import views as appViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('login/', appViews.Login),
    path('report-form/', views.ReportForm),
    path('report-form/add-report/', appViews.AddMonthlyReport),

    path('add-member/', views.AddMember),
    path('add-member/add/', appViews.AddMemberIntoModel),

    path('add-rukan/', views.AddRukan),
    path('add-rukan/add/', appViews.AddRukanIntoModel),

    path('add-umeedwar/', views.AddUmeedwar),
    path('add-umeedwar/add/', appViews.AddUmeedwarIntoModel),

    path('add-block-code/', views.AddBlockCode),
    path('add-block-code/add/', appViews.AddBlockCodeToModel),

    path('add-nc-goals/', views.AddNCGoals),
    path('add-nc-goals/add/', appViews.AddNCGoalIntoModel),

    path('admin-dashboard/', views.AdminDashboard),
    path('add-nc/', views.AddNC),
    path('add-nc/add/', appViews.AddNCToModel),
    path('add-extra-nc-program/', views.AddExtraNCProgram),
    path('add-extra-nc-program/add/', appViews.AddExtraNCProgramIntoModel),
]
