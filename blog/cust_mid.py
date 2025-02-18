from django.http import HttpResponseForbidden


class AdminAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the IP from REMOTE_ADDR or X-Forwarded-For
        ip = request.META.get('REMOTE_ADDR')
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]

        print(f"Request IP: {ip}")  # Print IP for debugging

        if request.path.startswith('/admin'):
            if ip not in ['127.0.0.1']:
                return HttpResponseForbidden("Access Forbidden")

        return self.get_response(request)
