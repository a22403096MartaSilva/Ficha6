import json
from portfolio.models import TFC, Tecnologia

with open("data/tfcs_2025.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados:
    tfc = TFC.objects.create(
        titulo=item["titulo"],
        autor=item["autor"],
        orientador=item["orientador"],
        curso=item["curso"],
        ano=item["ano"],
        resumo=item["resumo"],
        classificacao=item["rating"],
    )
    
    for nome in item["tecnologias_usadas"]:
        tecnologia, _ = Tecnologia.objects.get_or_create(
            nome=nome,
            defaults={
                "tipo": "",
                "descricao": "",
                "link_oficial": "",
                "nivel_preferencia": 0,
            }
        )
        tfc.tecnologias.add(tecnologia)
    





