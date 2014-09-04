# -*- coding: utf-8 -*-

from django.db import models
from generic.models import GenericModel, GenericStateModel, GenericStateModerable, FalseFK
from django.utils.translation import ugettext_lazy as _

from rights.utils import UnitEditableModel


class _WebsiteNews(GenericModel, GenericStateModerable, GenericStateModel, UnitEditableModel):

    class MetaRightsUnit(UnitEditableModel.MetaRightsUnit):
        access = None

    title = models.CharField(max_length=255)
    content = models.TextField()
    url = models.URLField(max_length=255)
    unit = FalseFK('units.models.Unit')

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class MetaData:
        list_display = [
            ('title', _('Titre')),
            ('start_date', _('Date debut')),
            ('end_date', _('Date fin')),
            ('status', _('Status')),
        ]
        details_display = list_display + [('content', _('Content')), ('url', _('URL'))]
        filter_fields = ('title', 'start_date', 'end_date', 'status')

        base_title = _('News AGEPoly')
        list_title = _(u'Liste de toutes les news sur le site de l\'AGEPoly')
        base_icon = 'fa fa-list'
        elem_icon = 'fa fa-bullhorn'

        menu_id = 'menu-communication-websitenews'

        datetime_fields = ['start_date', 'end_date']

        has_unit = True

    class MetaEdit:
        date_time_fields = ('start_date', 'end_date')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title
