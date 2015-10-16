from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, UpdateView)

from timepiece.utils.csv import CSVViewMixin
from timepiece.utils.search import SearchListView
from timepiece.utils.views import cbv_decorator

from itertools import groupby

from .forms import AddEditATACode, ATACodeSearchForm
from .models import ATACode

@cbv_decorator(permission_required('ata_codes.add_atacode'))
class AddATACode(CreateView):
    model = ATACode
    form_class = AddEditATACode
    success_url = reverse_lazy('list_ata_codes')
    template_name = 'ata_codes/add_edit.html'

@cbv_decorator(permission_required('ata_codes.delete_atacode'))
class DeleteATACode(DeleteView):
    model = ATACode
    success_url = reverse_lazy('list_ata_codes')
    pk_url_kwarg = 'ata_code_id'
    template_name = 'timepiece/delete_object.html'


@cbv_decorator(permission_required('ata_codes.change_atacode'))
class EditATACode(UpdateView):
    model = ATACode
    form_class = AddEditATACode
    pk_url_kwarg = 'ata_code_id'
    success_url = reverse_lazy('list_ata_codes')
    template_name = 'ata_codes/add_edit.html'

@cbv_decorator(permission_required('ata_codes.view_atacode'))
class ListATACodes(SearchListView, CSVViewMixin):
    model = ATACode
    form_class = ATACodeSearchForm
    redirect_if_one_result = False
    search_fields = ['name__icontains']
    template_name = 'ata_codes/list.html'

    def get(self, request, *args, **kwargs):
        self.export_ata_code_list = request.GET.get('export_ata_code_list', False)
        if self.export_ata_code_list:
            kls = CSVViewMixin

            form_class = self.get_form_class()
            self.form = self.get_form(form_class)
            self.object_list = self.get_queryset()
            self.object_list = self.filter_results(self.form, self.object_list)

            allow_empty = self.get_allow_empty()
            if not allow_empty and len(self.object_list) == 0:
                raise Http404("No results found.")

            context = self.get_context_data(form=self.form,
                object_list=self.object_list)

            return kls.render_to_response(self, context)
        else:
            kls = SearchListView

            form_class = self.get_form_class()
            self.form = self.get_form(form_class)
            self.object_list = self.get_queryset()
            self.object_list = self.filter_results(self.form, self.object_list)

            context = self.get_context_data(form=self.form,
                object_list=self.object_list)
            context['ata_codes'] = []
            for primary_ata, atas in groupby(self.object_list, lambda ata:ata.primary_ata_code):
                context['ata_codes'].append([primary_ata, list(atas)])

            return kls.render_to_response(self, context)

    def filter_form_valid(self, form, queryset):
        queryset = super(ListATACodes, self).filter_form_valid(form, queryset)
        primary_ata_code = form.cleaned_data['primary_ata_code']
        if primary_ata_code:
            queryset = queryset.filter(primary_ata_code=int(primary_ata_code))
        return queryset

    def get_filename(self, context):
        request = self.request.GET.copy()
        search = request.get('search', '(empty)')
        return 'ata_code_search_{0}'.format(search)

    def convert_context_to_csv(self, context):
        """Convert the context dictionary into a CSV file."""
        content = []
        ata_code_list = context['object_list']
        if self.export_ata_code_list:
            headers = ['Primary ATA Code', 'Secondary ATA Code', 'Name',
                       'Severity Factor', 'Last Date Changed'
                       ]
            content.append(headers)
            for ata_code in ata_code_list:
                row = [ata_code.primary_ata_code, ata_code.secondary_ata_code,
                       ata_code.name, ata_code.severity_factor,
                       ata_code.last_change_date]
                content.append(row)
        return content
