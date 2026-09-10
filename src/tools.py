import csv
import math


def get_data(base, scenario):
    if scenario not in {"01", "02", "03"}: raise ValueError("Escenario no autorizado")
    source = "datos/escenario_" + scenario + ".csv"
    with (base / source).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    proposals = []
    for row in rows:
        required = ["stock", "daily_demand", "lead_days", "safety_days", "incoming", "pack"]
        if any(row.get(k, "") == "" for k in required):
            proposals.append({"sku": row["sku"], "quantity": None, "action": "manual_review", "detail": "Faltan datos; no se supone un valor"})
            continue
        stock, demand, lead, safety, incoming, pack = [int(row[k]) for k in required]
        if min(stock, demand, lead, safety, incoming) < 0 or pack <= 0:
            raise ValueError("Dato numérico fuera de rango")
        target = demand * (lead + safety)
        needed = max(0, target - stock - incoming)
        quantity = math.ceil(needed / pack) * pack
        proposals.append({"sku":row["sku"], "quantity": quantity, "action":"buy" if quantity else "no_order",
            "detail":f"Objetivo {target}; stock {stock}; entrante {incoming}; múltiplo {pack}"})
    return {"scenario":scenario, "source":source, "raw_rows":rows, "proposals":proposals,
        "formula":"ceil(max(0, demanda_diaria*(plazo+seguridad)-stock-entrante)/bulto)*bulto"}


def validate(output, observation):
    problems=[]
    if output["scenario"] != observation["scenario"]: problems.append("Escenario incorrecto")
    actual=sorted([(p["sku"],p["quantity"],p["action"]) for p in output["proposals"]])
    expected=sorted([(p["sku"],p["quantity"],p["action"]) for p in observation["proposals"]])
    if actual != expected: problems.append("La propuesta no coincide con la herramienta")
    if output["requires_human_approval"] is not True: problems.append("Falta aprobación humana")
    return problems
