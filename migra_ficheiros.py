

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.files import File
from portfolio.models import Projeto

for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = obj.imagem.path

        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                obj.imagem.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print("Migrado:", obj)