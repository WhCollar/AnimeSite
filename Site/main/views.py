from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters import BaseInFilter, CharFilter, FilterSet
from django_filters.views import FilterView
from main.models import *


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass


class CatalogSearchFilter(FilterSet):
    status = CharFilter(field_name='status__title')
    age_rating = CharFilter(field_name='age_rating__title')
    content_type = CharFilter(field_name='content_type__title')
    genre = CharFilterInFilter(field_name='genre__title', lookup_expr='in')
    title = CharFilter(field_name='q')

    class Meta:
        model = Content
        fields = ['status', 'age_rating', 'content_type', 'genre', 'title']


class Catalog(FilterView):
    model = Content
    template_name = 'main/catalog.html'
    context_object_name = 'catalog'
    paginate_by = 10
    filterset_class = CatalogSearchFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = Status.objects.all()
        context['age_rating'] = Age_rating.objects.all()
        context['genre'] = Genre.objects.all()
        context['content_type'] = Content_type.objects.all()
        context['title'] = 'Catalog'
        return context


def index(request):
    return render(request, 'main/index.html')


class GetItem(DetailView):
    model = Content
    template_name = 'main/single_item.html'
    context_object_name = 'item'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Content.objects.get(slug=self.kwargs['slug'])
        return context
