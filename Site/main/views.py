from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django_filters import BaseInFilter, CharFilter, FilterSet
from django_filters.views import FilterView
from main.forms import RegisterUserForm, LoginUserForm
from django.http import JsonResponse
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


def profile(request):
    return render(request, 'main/profile.html')


class GetItem(DetailView):
    model = Content
    template_name = 'main/single_item.html'
    context_object_name = 'item'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Content.objects.get(slug=self.kwargs['slug'])
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context


"""Ассинхронные запросы (AJAX)"""


def ajax_buttons_for_add_or_delete_to_lists(request):
    user = User.objects.get(username=request.GET.get('user_nickname', None))
    content = Content.objects.get(slug=request.GET.get('content_slug', None))
    like = request.GET.get('like_bool', None)
    watching = request.GET.get('watching_bool', None)
    will_be_watching = request.GET.get('will_be_watching_bool', None)
    abandoned = request.GET.get('abandoned_bool', None)
    response = {
        'like_bool': False,
        'watching_bool': False,
        'will_be_watching_bool': False,
        'abandoned_bool': False,
    }
    """Если на фронтенде поставлен лайк, то создаём запись о том, что пользователь добавил тайтл в любимое, иначе
    проверяем существует ли запись о том, тайтл в любимом, если да удаляем, если нет, забиваем болт"""
    if like == 'true':
        add_to_like_list = ContentList(list_type=ListType.objects.get(title='Любимые'),
                                       content=content,
                                       user=user)
        add_to_like_list.save()

        response['like_bool'] = True
    elif like == 'false':
        if ContentList.objects.filter(list_type=ListType.objects.get(title='Любимые'),
                                      content=content,
                                      user=user).exists():
            obj = ContentList.objects.get(list_type=ListType.objects.get(title='Любимые'),
                                          content=content,
                                          user=user)
            obj.delete()

            response['like_bool'] = False

    return JsonResponse(response)
