def get_current_host(request) -> str:
    ''' Returns the host url with current scheme '''
    scheme = request.is_secure() and "https" or "http"
    return f"{scheme}://{request.get_host()}"


def generate_full_url(
    request, instance, instance_user=False, instance_profile=None
) -> str:
    """Returns the full instance url
    instance_user => profile.user
    instance_profile => user.profile

    if we want the User url if instance=Profile, pass instance_user
    if we want the Profile url if instance=User, pass instance_profile
    """
    if (
        instance_user
    ):  # instance is Profile. (url for instance.user one to one relationship (user instance url))
        host = get_current_host(request=request)
        instance_url = instance.user.get_absolute_url()  # defined in model
        return host + instance_url
    elif instance_profile:  # instance is User
        host = get_current_host(request=request)
        instance_url = instance.profile.get_absolute_url()
        return host + instance_url
    else:  # general instance url
        host = get_current_host(request=request)
        instance_url = instance.get_absolute_url()
        return host + instance_url
