from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        if request.user.groups.filter(name='Hindi_Manager').exists():
            return qs.filter(subject='Hindi')

        if request.user.groups.filter(name='English_Manager').exists():
            return qs.filter(subject='English')

        if request.user.groups.filter(name='Math_Manager').exists():
            return qs.filter(subject='Math')

        if request.user.groups.filter(name='Science_Manager').exists():
            return qs.filter(subject='Science')

        return qs.none()

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Subject, SubjectAdmin)