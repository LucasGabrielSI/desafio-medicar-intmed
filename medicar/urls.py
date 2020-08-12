from django.contrib import admin
from django.urls import path

from users import views as users_views
from doctors import views as doctors_views
from schedule import views as schedule_views
from specialties import views as specialties_views
from consultation import views as consultation_views

admin.site.site_header = 'Medicar'
admin.site.index_title = 'Medicar Administração'
admin.site.site_title = 'Administração'

urlpatterns = [
    path('', admin.site.urls),
    path('especialidades/', specialties_views.SpecialtiesList.as_view()),
    path('medicos/', doctors_views.DoctorsList.as_view()),
    path('agendas/', schedule_views.ScheduleList.as_view()),
    path('consultas/', consultation_views.ConsultationList.as_view()),
    path('consultas/<int:pk>/', consultation_views.ConsultationDestroy.as_view()),
    path('usuarios/cadastro/', users_views.UsersCreate.as_view()),
    path('usuarios/login/', users_views.UsersLogin.as_view()),
]
