from django.urls import path
from . import views

urlpatterns = [
    path('', views.TravelHome.as_view(), name="travelhome"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('country/', views.ViewCountry.as_view(), name='country_list'),
    path('country/new/', views.CountryCreate.as_view(), name="country_create"),
    path('country/<int:pk>', views.CountryDetail.as_view(), name="country_detail"),
    path('country/<int:pk>/update', views.CountryUpdate.as_view(), name="country_update"),
    path('country/<int:pk>/delete', views.CountryDelete.as_view(), name="country_delete"),
    path('city/', views.CityList.as_view(), name = "city_list"),
    path('country/<int:pk>/city/new', views.CityCreate.as_view(), name="city_create"),
    path('favorite/<int:pk>/city/<int:city_pk>/', views.FavoriteCityAssoc.as_view(),name="favorite_city_assoc"),
    path('favorite/new/', views.FavoriteCreate.as_view(),name="favorite_create"),
    path('favorite/<int:pk>/delete',views.FavoriteDelete.as_view(),name="favorite_delete")
]