"""Валидация загружаемых файлов (ТЗ раздел 32):
только PDF/JPG/PNG, проверка размера."""

import re

from django.conf import settings
from django.core.exceptions import ValidationError

IIN_PATTERN = re.compile(r"^\d{12}$")


def validate_iin(value):
    if not value or not IIN_PATTERN.match(str(value)):
        raise ValidationError("ИИН должен содержать ровно 12 цифр.")
    return value


def validate_upload(file):
    ext = file.name.rsplit(".", 1)[-1].lower() if "." in file.name else ""
    if ext not in settings.ALLOWED_UPLOAD_EXTENSIONS:
        raise ValidationError(
            f"Недопустимый тип файла. Разрешены: {', '.join(settings.ALLOWED_UPLOAD_EXTENSIONS)}"
        )
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if file.size > max_bytes:
        raise ValidationError(f"Файл больше {settings.MAX_UPLOAD_SIZE_MB} МБ")
    return file
