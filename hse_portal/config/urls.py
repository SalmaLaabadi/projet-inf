from django.contrib import admin
from django.urls import path, include
from excelhub.views import dashboard, excel_home, excel_by_date

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentification (login/logout prêt à l’emploi)
    path('accounts/', include('django.contrib.auth.urls')),

    # Tableau de bord
    path('dashboard/', dashboard, name='dashboard'),

    # Gestion des fichiers Excel
    path('excel/', excel_home, name='excel_home'),
    path('excel/<str:yyyy_mm_dd>/', excel_by_date, name='excel_by_date'),
]
