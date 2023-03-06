from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from my_app import views as app

urlpatterns = [
    path('', app.form_view, name='loginform'),
    path('login/form/', app.login_page, name="login"),
    path('register/new/user/', app.register_user, name="reg"),
    path('listing/product/page/', app.dashbord_page, name='product_listing'),
    path('logout/user/', app.delete_session, name="logout")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
