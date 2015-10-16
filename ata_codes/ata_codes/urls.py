from django.conf.urls import patterns, url

from .views import AddATACode, DeleteATACode, EditATACode, ListATACodes

urlpatterns = patterns('',
    url(r'^$',
        ListATACodes.as_view(),
        name='list_ata_codes'),
    url(r'^add/$',
        AddATACode.as_view(),
        name='add_ata_code'),
    url(r'^(?P<ata_code_id>\d+)/edit/$',
        EditATACode.as_view(),
        name='edit_ata_code'),
    url(r'^(?P<ata_code_id>\d+)/delete/$',
        DeleteATACode.as_view(),
        name='delete_ata_code'),
)
