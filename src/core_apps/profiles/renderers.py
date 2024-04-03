import json 
from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer): 
    ''' Profile JSON Renderer for single object. '''
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None: 
            status_code = 200 
        else: 
            status_code = renderer_context.get('response').status_code

        # in case of DELETE request, the "data" will be None else "data" will hold queryset or error codes
        if data is not None: 
            errors = data.get('errors', None)
        else: 
            errors = None 

        # if there are errors, then render as per default JSON style.
        if errors is not None: 
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({'status_code':status_code, 'profile':data})


class MultiProfileJSONRenderer(JSONRenderer):
    """Profile JSON Renderer for single object."""

    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None:
            status_code = 200
        else:
            status_code = renderer_context.get("response").status_code

        errors = data.get("errors", None)
   

        # if there are errors, then render as per default JSON style.
        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "profiles": data})
