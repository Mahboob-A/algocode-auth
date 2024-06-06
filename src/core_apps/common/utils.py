from urllib.parse import urlparse

def get_current_host(request) -> str:
    """Returns the host url with current scheme"""

    scheme = "https" if request.is_secure() else "http"
    host = request.get_host()

    parsed_host = urlparse(f"{scheme}://{host}")
    hostname = parsed_host.hostname

    if hostname in ["127.0.0.1", "localhost"]:
        port = 8000
        return f"{scheme}://{hostname}:{port}"
    else:
        return f"{scheme}://{hostname}"

    # scheme = request.is_secure() and "https" or "http"
    # if host is localhost, add 8000 as port. else do not add any port.
    # if request.get_host() == "127.0.0.1": 
    #     port = 8000
    #     return f"{scheme}://{request.get_host()}:{port}"
    # else: 
    #     return f"{scheme}://{request.get_host()}"


def generate_full_url(
    request, instance, instance_user=False, instance_profile=None
) -> str:
    """Returns the full instance url
    instance_user => profile.user
    instance_profile => user.profile

    if we want the User url if instance=Profile, pass instance_user
    if we want the Profile url if instance=User, pass instance_profile

    example instance_url: /api/v1/profiles/profile/34735ef8-1e0a-4bb1-b41c-93e70eb358b1/
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
