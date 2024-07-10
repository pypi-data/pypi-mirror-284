from typing import List, Dict

class CsvExporter(Exporter):
    def export(self, data: List[Dict], file_path: str) -> str:
        return f"Data exported to {file_path}"
