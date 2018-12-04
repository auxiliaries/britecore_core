from django.contrib import admin

from .models import RiskType, FieldImplementation, FieldChoice

# Register your models here.


class FieldImplementationInline(admin.StackedInline):
    model = FieldImplementation

    list_display = ('risk_type', "title", )


class RiskTypeAdmin(admin.ModelAdmin):
    model = RiskType

    inlines = (FieldImplementationInline, )


admin.site.register(RiskType, RiskTypeAdmin)


class FieldChoiceInLine(admin.StackedInline):
    model = FieldChoice

    list_display = ('field', "title", )


class FieldImplementationAdmin(admin.ModelAdmin):
    model = FieldImplementation

    list_display = ('risk_type', "title", )

    inlines = (FieldChoiceInLine, )


admin.site.register(FieldImplementation, FieldImplementationAdmin)
