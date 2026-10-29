import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {"Count": len(values), "Smallest": min(values), "Largest": max(values), "average": sum(values) / len(values),}
def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarise_all("ETIOSA_WARD.csv", ["AREA"])

for column, summary in report.items():
    print(column, "->", summary)

import csv
from collections import Counter

def read_rows(filename):
    with open(filename, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clean_values(rows, column):
    values = []

    for row in rows:
        raw = row.get(column, "")

        if raw is None or raw.strip() == "":
            continue

        values.append(raw.strip())

    return values


def summarise(values):
    if len(values) == 0:
        return {
            "Total records": 0,
            "Unique wards": 0,
            "Ward frequency": {}
        }

    ward_counts = Counter(values)

    return {
        "Total records": len(values),
        "Unique wards": len(ward_counts),
        "Ward frequency": dict(sorted(ward_counts.items()))
    }


def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}

    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)

    return report


# Summarize wardname column
report = summarise_all("ETIOSA_WARD.csv", ["wardname"])


# Display summary
for column, summary in report.items():
    print(f"\nSUMMARY FOR {column.upper()}")
    print("-" * 40)

    print("Total records:", summary["Total records"])
    print("Unique wards:", summary["Unique wards"])

    print("\nWard Frequency:")

    for ward, count in summary["Ward frequency"].items():
        print(f"{ward}: {count}")