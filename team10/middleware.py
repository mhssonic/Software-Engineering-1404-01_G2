from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render


class Team10ErrorPageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Http404:
            if request.path.startswith("/team10/"):
                return render(request, "team10/404.html", status=404)
            raise
        except PermissionDenied:
            if request.path.startswith("/team10/"):
                return render(request, "team10/404.html", status=403)
            raise

        if request.path.startswith("/team10/") and response.status_code in (403, 404):
            return render(request, "team10/404.html", status=response.status_code)

        return response
