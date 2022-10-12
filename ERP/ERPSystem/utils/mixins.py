from django.http import JsonResponse

class AjaxResponseMixin(object):
    def form_invalid(self, form):
        response = super(AjaxResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = {
                'state': 'error',
                'msg': form.errors
            }
            return JsonResponse(data, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'state': 'success'
            }
            return JsonResponse(data)
        else:
            return response