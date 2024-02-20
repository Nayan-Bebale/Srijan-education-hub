from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from desktop.views import index

from django.contrib.auth import views as auth_views
from searches.views import search_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'), 
    path('desktop/', include('desktop.urls', namespace='desktop')),
    path('chatsystem/', include('chatsystem.urls', namespace='chatsystem')),
    path('search/', search_view, name="search_view"),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registrations/reset_password.html"),
        name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registrations/reset_password_sent.html"),
          name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registrations/reset.html"),
          name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registrations/reset_password_complete.html"), 
         name="password_reset_complete"),
        
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)
