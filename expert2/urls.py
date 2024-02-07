from django.contrib import admin
from django.urls import path
from expert_em_cifras import views

urlpatterns = [
    path('', views.index, name='expert_em_cifras'),
    path('expert_EmCifras', views.expertEmCifras, name='expertEmCifras'),
    path('admin/', admin.site.urls),

]
