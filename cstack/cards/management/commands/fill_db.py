import os

from django.core.management.base import BaseCommand
from django.core.files.uploadedfile import SimpleUploadedFile
from cards.models import Card, CardCategory
from PIL import Image


class Command(BaseCommand):

    help = "Fill Db"

    def handle(self, *args, **kwargs):

        # Создание категорий карт
        categories = [
            "album",
            "extra",
            "caratzone",
            "concert trading",
            "caratland trading",
            "dvd",
            "broadcast",
            "membership",
            "other",
        ]
        for category_name in categories:
            CardCategory.objects.get_or_create(name=category_name)

        # Создание карт
        cards_data = [
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2015,
                "release_country": "korea",
                "album": "boys be",
                "description": "wonwoo hide ver.",
                "shop": "",
                "image_path": "media/card_images/ww_boys_be_1.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2015,
                "release_country": "korea",
                "album": "boys be",
                "description": "wonwoo seek ver.",
                "shop": "",
                "image_path": "media/card_images/ww_boys_be_2.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "love&letter repackage ver.",
                "description": "wonwoo love&letter 1",
                "shop": "",
                "image_path": "media/card_images/ww_ll_1.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "love&letter repackage ver.",
                "description": "wonwoo love&letter 2",
                "shop": "",
                "image_path": "media/card_images/ww_ll_2.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "going seventeen",
                "description": "wonwoo going svt wish ver.",
                "shop": "",
                "image_path": "media/card_images/ww_going_svt_1wish.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "going seventeen",
                "description": "wonwoo going svt happen ver.",
                "shop": "",
                "image_path": "media/card_images/ww_going_svt_2happen.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "going seventeen",
                "description": "wonwoo going svt seventeen ver.",
                "shop": "",
                "image_path": "media/card_images/ww_going_svt_3svt.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "going seventeen",
                "description": "wonwoo going svt wish ver. wonwoo-jeonghan unit card",
                "shop": "",
                "image_path": "media/card_images/ww_going_svt_4wwjh.jpg",
            },
            {
                "name": "wonwoo",
                "category": CardCategory.objects.get(name="album"),
                "release_year": 2016,
                "release_country": "korea",
                "album": "going seventeen",
                "description": "wonwoo going svt wish ver. wonwoo-mingyu unit card",
                "shop": "",
                "image_path": "media/card_images/ww_going_svt_5wwmg.jpg",
            },
        ]

        for card_data in cards_data:
            image_path = card_data.pop("image_path")
            image_name = os.path.basename(image_path)
            with open(image_path, "rb") as f:
                image = SimpleUploadedFile(
                    image_name, f.read(), content_type="image/jpeg"
                )
                card_data["image"] = image
                Card.objects.create(**card_data)

        self.stdout.write(self.style.SUCCESS("DB is ready"))
