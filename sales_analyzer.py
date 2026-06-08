
"""
sales_analyzer.py
 
Reads sales_data.csv, computes summary statistics, and writes two outputs:
  - sales_report.txt     (human-readable summary)
  - product_summary.csv  (machine-readable per-product totals)
"""
 
import csv
from collections import defaultdict
 
INPUT_FILE = "sales_data.csv"
REPORT_FILE = "sales_report.txt"
SUMMARY_CSV = "product_summary.csv"
 
 
def read_sales(path):
    """Read the CSV and return a list of row dicts with numeric fields converted."""
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)          # uses the header row for keys
        for row in reader:
            # DictReader gives every value as a string, so convert what we need
            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])
            row["revenue"] = row["quantity"] * row["price"]
            rows.append(row)
    return rows
 
 
def analyze(rows):
    """Compute all the totals from the list of rows."""
    total_revenue = 0.0
    revenue_by_product = defaultdict(float)
    quantity_by_product = defaultdict(int)
    revenue_by_day = defaultdict(float)
 
    for row in rows:
        total_revenue += row["revenue"]
        revenue_by_product[row["product"]] += row["revenue"]
        quantity_by_product[row["product"]] += row["quantity"]
        revenue_by_day[row["date"]] += row["revenue"]
 
    # The day whose accumulated revenue is largest.
    # max() with key=... compares dates by their revenue value, not alphabetically.
    best_day = max(revenue_by_day, key=revenue_by_day.get)
 
    return {
        "total_revenue": total_revenue,
        "revenue_by_product": revenue_by_product,
        "quantity_by_product": quantity_by_product,
        "revenue_by_day": revenue_by_day,
        "best_day": best_day,
    }
 
 
def write_report(stats, path):
    """Write a formatted, human-readable summary."""
    with open(path, "w") as f:
        f.write("SALES REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total revenue: ${stats['total_revenue']:,.2f}\n\n")
 
        f.write("Revenue by product:\n")
        for product in sorted(stats["revenue_by_product"]):
            f.write(f"  {product:<12} ${stats['revenue_by_product'][product]:>10,.2f}\n")
        f.write("\n")
 
        f.write("Quantity sold by product:\n")
        for product in sorted(stats["quantity_by_product"]):
            f.write(f"  {product:<12} {stats['quantity_by_product'][product]:>5} units\n")
        f.write("\n")
 
        best = stats["best_day"]
        f.write(f"Best day: {best} (${stats['revenue_by_day'][best]:,.2f})\n")
 
 
def write_summary_csv(stats, path):
    """Write a per-product summary CSV."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "total_quantity", "total_revenue"])  # header
        for product in sorted(stats["revenue_by_product"]):
            writer.writerow([
                product,
                stats["quantity_by_product"][product],
                f"{stats['revenue_by_product'][product]:.2f}",
            ])
 
 
def main():
    rows = read_sales(INPUT_FILE)
    stats = analyze(rows)
    write_report(stats, REPORT_FILE)
    write_summary_csv(stats, SUMMARY_CSV)
 
    # A little console feedback so you know it ran
    print(f"Read {len(rows)} rows from {INPUT_FILE}")
    print(f"Total revenue: ${stats['total_revenue']:,.2f}")
    print(f"Best day: {stats['best_day']} "
          f"(${stats['revenue_by_day'][stats['best_day']]:,.2f})")
    print(f"Wrote {REPORT_FILE} and {SUMMARY_CSV}")
 
 
if __name__ == "__main__":
    main()
 