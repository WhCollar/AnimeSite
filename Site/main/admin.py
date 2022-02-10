from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class ContentAdminForm(forms.ModelForm):
    synopsis = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = '__all__'


class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class Age_ratingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class Dubbing_studioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class Content_typeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = ContentAdminForm
    search_fields = ('title',)
    list_filter = ('status',)


admin.site.register(Status, StatusAdmin)
admin.site.register(Age_rating, Age_ratingAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Dubbing_studio, Dubbing_studioAdmin)
admin.site.register(Content_type, Content_typeAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(IframeForContent)
admin.site.register(VideoPlayer)
admin.site.register(ListType)
admin.site.register(UserProfiles)
admin.site.register(ContentList)
