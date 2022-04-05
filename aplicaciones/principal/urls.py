from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home,  name="home"),
    path('calendar/', views.calendar,name="calendar"),
    path('register/',views.register ,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('crear_ingreso/', views.crearIngreso,name="ingreso"),
    path('update_ingreso/<str:pk>/', views.updateIngreso,name="update_ingreso"),
    path('delete_ingreso/<str:pk>/', views.deleteIngreso,name="delete_ingreso"),
    path('crear_gasto/',views.crearGasto,name="gastos"), 
    path('update_gasto/<str:pk>/', views.updateGasto,name="update_gasto"),
    path('delete_gasto/<str:pk>/', views.deleteGasto,name="delete_gasto"),
    path('ingresos/', views.ingresos,name="ingresos"),
    path('gasto/', views.gasto,name="gasto"),
    path('config/', views.config,name="config"),
    path('ingresos_chart/', views.ingresosChart, name='ingresos_chart'),
    path('gastos_chart/', views.gastosChart, name='gastos_chart'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='principal/password_change.html'),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='principal/password_change_done.html'),name='password_change_done'),

    path ('reset_password/',auth_views.PasswordResetView.as_view(template_name="principal/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="principal/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="principal/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="principal/password_reset_done.html"), name="password_reset_complete"),
]
