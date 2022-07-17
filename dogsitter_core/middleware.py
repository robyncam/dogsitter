from django.shortcuts import redirect, reverse
from django.contrib import messages


class ProfileMiddleware:
    URL_EXCEPTIONS = ['profile', 'logout']

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path not in [reverse(name) for name in self.URL_EXCEPTIONS]:
            if request.user.is_authenticated and not hasattr(request.user, 'profile'):
                messages.warning(request, "Please create a profile before continuing")
                return redirect('profile')

        response = self.get_response(request)

        return response
