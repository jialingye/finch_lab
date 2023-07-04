from typing import Any, Dict
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
# import models
from .models import Country, City, Favorite
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
# class Home(View):

#     # Here we are adding a method that will be ran when we are dealing with a GET request
#     def get(self, request):
#         # Here we are returning a generic response
#         # This is similar to response.send() in express
#         return HttpResponse("Home")

class About(View):
    def get(self, request):
        return HttpResponse("ViewScreen")

class TravelHome(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

class ViewCountry(TemplateView):
    template_name = 'country_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['countries'] = Country.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["countries"] = Country.objects.all()
            context['header'] = "Traveled Countries"
        return context

class CountryCreate(CreateView):
    model = Country
    fields = ['name', 'img', 'bio', 'travel_again']
    template_name = "country_create.html"
    success_url = "/country/"

class CountryDetail(DetailView):
    model = Country
    template_name = "country_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

class CountryUpdate(UpdateView):
    model = Country
    fields = ['name', 'img', 'bio', 'travel_again']
    template_name = "country_update.html"

    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})

class CountryDelete(DeleteView):
    model = Country
    template_name = 'country_delete_confirmation.html'
    success_url = '/country'

class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["citys"] = City.objects.all()
        return context
    
class CityCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        population = request.POST.get("population")
        country = Country.objects.get(pk = pk)
        City.objects.create(name=name, population=population, country=country)
        return redirect('country_detail', pk=pk)

class FavoriteCityAssoc(View):
    def get(self,request,pk, city_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Favorite.objects.get(pk=pk).citys.remove(city_pk)
        if assoc == "add":
            Favorite.objects.get(pk=pk).citys.add(city_pk)
        return redirect('travelhome')

class FavoriteCreate(CreateView):
    model = Favorite
    fields = ['title']
    template_name = "favorite_create.html"
    success_url = "/"

class FavoriteDelete(DeleteView):
    model = Favorite
    template_name = 'favorite_delete_confirmation.html'
    success_url = '/'