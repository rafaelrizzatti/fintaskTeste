from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Demanda(models.Model):
    anunciante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.CharField(_("Descricao"), max_length=255)
    endereco = models.CharField(_("Endereco"), max_length=255)
    info_contato = models.CharField(_("info_contato"), max_length=255)
    status = models.BooleanField(_("Status"), default=False)
    data_criacao = models.DateTimeField(_("data_criacao"), auto_now_add=True)

    class Meta:
        verbose_name = _("Demanda")
        verbose_name_plural = _("Demandas")

    def __unicode__(self):
        return smart_unicode(self.descricao)
