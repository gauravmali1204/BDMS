from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from .models import profile

def role_required(allowed_roles):
    """
    Decorator to check if user has required role.
    allowed_roles: list of role strings like ['ADMIN', 'MANAGER']
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, 'Please login to access this page.')
                return redirect('login')

            try:
                user_profile = request.user.profile
                if user_profile.role not in allowed_roles:
                    messages.error(request, 'You do not have permission to access this page.')
                    return redirect('dashboard')  # or appropriate redirect
            except profile.DoesNotExist:
                messages.error(request, 'Profile not found. Please contact administrator.')
                return redirect('login')

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# Specific role decorators
def admin_required(view_func):
    return role_required(['ADMIN'])(view_func)

def manager_required(view_func):
    return role_required(['ADMIN', 'MANAGER'])(view_func)

def staff_required(view_func):
    return role_required(['ADMIN', 'MANAGER', 'STAFF'])(view_func)