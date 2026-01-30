from template import *

def main():
    data = {"title": "Sales Report", "content": ["Item1: $10", "Item2: $20"]}
    csv_exporter = CSVExport()
    csv_exporter.export_report(data, "report.csv")
    pdf_exporter = PDFExport()
    pdf_exporter.export_report(data, "report.pdf")

if __name__ == "__main__":
    main()