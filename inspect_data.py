import csv
import string
from turtle import st
with open("ETIOSA_WARD.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print("Number of rows:", len(rows))
print("Columns:", list(rows[0] .keys()))

import csv
with open("ETIOSA_WARD.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values = []
for row in rows:
    value = float(row["AREA"])
    values.append(value)

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv
with open("ETIOSA_WARD.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values = []
for row in rows:
    values = []
for row in rows:
    raw = row["AREA"].strip()
    if raw == "":
        continue
    values.append(float(raw))

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv
def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {"Smallest": min(values), "Largest": max(values), "Count": len(values)}

result = inspect_column("ETIOSA_WARD.csv", "AREA")
print(result)

import csv
def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(raw.strip())
    return {"Smallest": min(values), "Largest": max(values), "Count": len(values)}

wardname_result = inspect_column("ETIOSA_WARD.csv", "wardname")
lganame_result = inspect_column("ETIOSA_WARD.csv", "lganame")
print("wardname:", wardname_result)
print("lganame:", lganame_result)

