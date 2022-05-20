from django.conf import settings
from django.http import HttpResponseForbidden


class AdminProtect:
    """
    許可されていないip以外は管理サイトにアクセスできないようにする
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.get_full_path()

        if settings.ADMIN_PATH in url and not settings.DEBUG:

            ip_list = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip_list:
                ip = ip_list.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            if ip not in settings.ALLOWED_ADMIN:
                return HttpResponseForbidden()

        response = self.get_response(request)

        return response
