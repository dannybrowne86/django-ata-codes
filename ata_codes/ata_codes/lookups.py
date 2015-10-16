from selectable.base import LookupBase
from selectable.base import ModelLookup
from selectable.registry import registry

from django.db.models import Q

from .models import ATACode

class ATACodeLookup(LookupBase):
    # model = ATACode
    # search_fields = ('primary_ata_code', 'name__icontains', )

    def query(self, request, term):
    	try:
    		atacode = int(term)
    		return ATACode.objects.filter(primary_ata_code=atacode)
    	except:
    		return ATACode.objects.filter(name__icontains=term)

    def get_item_label(self, atacode):
        return mark_safe(u'<span class="project">%s</span>' %
                self.get_item_value(atacode))

    def get_item_value(self, atacode):
        return str(atacode) if atacode else ''

registry.register(ATACodeLookup)
