from django.urls import path,include
from . import views

urlpatterns = [
path('list/',views.ProductViewSets.as_view({"get":"list"})),
path('create/',views.ProductViewSets.as_view({"post":"create"})),
path('create_category/',views.CategoryViewSets.as_view({"post":"create"})),

]