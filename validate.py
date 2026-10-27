#!/usr/bin/env python3
"""Validador: python3 validate.py (en la carpeta con foods.json y exercises.json)"""
import json,sys,collections
bad=[];fo=json.load(open("foods.json"))["foods"];ex=json.load(open("exercises.json"))["exercises"]
for L,k in((fo,"id"),(ex,"id")):
    d=[x for x,c in collections.Counter(i[k] for i in L).items() if c>1]
    if d:bad.append(f"ids duplicados: {d}")
for L,k in((fo,"name_es"),(ex,"name_es")):
    d=[x for x,c in collections.Counter(i[k].lower() for i in L).items() if c>1]
    if d:bad.append(f"nombres duplicados: {d}")
for f in fo:
    for k in("kcal","protein_g","carbs_g","fat_g"):
        if not isinstance(f[k],(int,float)) or f[k]<0:bad.append(f"{f['id']} {k} inválido")
    if f["kcal"]>900 or f["protein_g"]+f["carbs_g"]+f["fat_g"]>100.5:bad.append(f"{f['id']} {f['name_es']}: valores imposibles")
    est=4*f["protein_g"]+4*f["carbs_g"]+9*f["fat_g"]
    if f["kcal"]>20 and abs(est-f["kcal"])/f["kcal"]>0.25:print(f"AVISO kcal vs macros ({est:.0f} vs {f['kcal']:.0f}): {f['name_es']}")
for e in ex:
    for k in("name_es","primary_muscle","equipment","movement_pattern"):
        if not e.get(k):bad.append(f"{e['id']} sin {k}")
print(f"alimentos: {len(fo)} | ejercicios: {len(ex)}")
if len(fo)<300:print("AVISO: menos de 300 alimentos")
if len(ex)<100:bad.append("menos de 100 ejercicios")
print("ERRORES:",*bad,sep="\n- ") if bad else print("Sin errores estructurales")
sys.exit(1 if bad else 0)
