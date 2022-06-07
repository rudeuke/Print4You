"""myproject URL Configuration

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
from django.urls import path, include
from register.views import AddressEditView
from register import views as v
from print4you import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from register.views import UserEditView

urlpatterns = [

    path('', v.homepage_redirect, name='homepage_redirect'),
    path('homepage/', v.homepage, name='homepage'),
    path('about/', v.about, name='about'),
    path('order/', views.order, name='order'),
    path('offer/', views.offer, name='offer'),
    path('app/', include('print4you.urls')),
    path("register/", v.register, name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path('address_redirect/', v.address_redirect),
    path("set_address/", v.add_address, name="set_address"),
    path("edit_address/", AddressEditView.as_view(), name="edit_address"),
    path('admin/', admin.site.urls),
    path("login/", v.login_request, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile", views.profile_view, name="profile"),
    path("accounts/login/", v.login_request, name='login'),
    path("calculator/", views.calculator, name='calculator'),
    path('update_printout/<str:pk>/',
         views.updatePrintout, name="update_printout"),
    path('neworder/<str:pk>/', views.newOrder, name="new_order"),
    path('payment/<str:pk>/', views.payment, name="payment"),
    path('', include("django.contrib.auth.urls")),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path(
        'password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change_password.html',
            success_url='/'
        ),
        name='password'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
