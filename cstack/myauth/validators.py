from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size_mb = 20
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"file size must not exceed 20mb{max_size_mb}mb")
