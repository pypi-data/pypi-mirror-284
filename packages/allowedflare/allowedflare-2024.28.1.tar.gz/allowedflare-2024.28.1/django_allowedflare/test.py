import django_allowedflare

def test_allowedflare_login_view(request):
    django_allowedflare.AllowedflareLoginView().get(request)
