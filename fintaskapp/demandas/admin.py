from django.contrib import admin
from demandas.models import Demanda


class DemandaAdmin(admin.ModelAdmin):
    list_display = ("anunciante", "descricao", "endereco", "info_contato", "status_view", "data_criacao")
    list_filter = ("anunciante", "data_criacao")

    def status_view(self, obj):
        from django.utils.html import format_html
        yes_icon = '<img src="/static/admin/img/baseline-check_circle_outline.svg" alt="True">'
        no_icon = '<img src="/static/admin/img/baseline-highlight_off.svg" alt="False">'
        if obj.status:
            return format_html(yes_icon)
        else:
            return format_html(no_icon)
    status_view.short_description = "status"


admin.site.register(Demanda, DemandaAdmin)
