from django.core.cache import cache
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import send_welcome_email_task

STATS_CACHE_KEY = "stats_data"

class StatsView(APIView):
    def get(self, request):
        cached_data = cache.get(STATS_CACHE_KEY)
        if cached_data is not None:
            return Response(
                {**cached_data, "cached": True},
                status=status.HTTP_200_OK,
            )

        data = {
            "users_count": 1000,
            "active_orders": 42,
        }
        cache.set(STATS_CACHE_KEY, data, timeout=60)

        return Response(
            {**data, "cached": False},
            status=status.HTTP_200_OK,
        )

class RegisterView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email or not isinstance(email, str) or "@" not in email:
            return Response(
                {"error": "Укажите корректный email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        send_welcome_email_task.delay(email)

        return Response(
            {
                "message": "Пользователь зарегистрирован, письмо ставится в очередь на отправку.",
                "email": email,
            },
            status=status.HTTP_201_CREATED,
        )