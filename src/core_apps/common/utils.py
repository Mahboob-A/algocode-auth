def get_current_host(request) -> str:
    ''' Returns the host url with current scheme '''
    scheme = request.is_secure() and "https" or "http"
    return f"{scheme}://{request.get_host()}"


def generate_full_url(request, instance, instance_user=False) -> str:
    ''' Returns the full instance url '''
    
    if instance_user:  # url for instance.user one to one relationship (user instance url)
        host = get_current_host(request=request)
        instance_url = instance.user.get_absolute_url()  # defined in model 
        return host + instance_url 
    else: # general instance url 
        host = get_current_host(request=request)
        instance_url = instance.get_absolute_url()
        return host + instance_url 