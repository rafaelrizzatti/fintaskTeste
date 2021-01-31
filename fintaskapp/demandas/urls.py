from django.urls import path
from demandas.views import DemandasListCreate, DemandaCrud, DemandaFinalizar

app_name = 'demandas'

urlpatterns = [
    path('', DemandasListCreate.as_view(), name="list"),
    path('<int:pk>/finalizar/', DemandaFinalizar.as_view(), name="finish"),
    path('<int:pk>/', DemandaCrud.as_view(), name="detail"),
]
