import logging
import time
from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email_task(user_email: str) -> str:
    """Имитирует отправку приветственного письма с задержкой 5 секунд."""
    logger.info(f"Начинаю отправку письма на {user_email}...")
    time.sleep(5)
    message = f"Приветственное письмо отправлено на {user_email}"
    logger.info(message)
    print(message, flush=True)
    return message


@shared_task
def clear_expired_cache_task() -> None:
    """Периодическая задача (раз в 1 минуту)."""
    print("Beat Task: Cleaning expired items...", flush=True)