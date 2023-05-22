# api_survey/middleware.py
from django.http import HttpResponseForbidden
from .models import AllowedIps

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        if not AllowedIps.objects.filter(ip_address = client_ip).exists():
            return HttpResponseForbidden('Acceso denegado')

        return self.get_response(request)