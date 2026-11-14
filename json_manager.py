import json
from pathlib import Path

# პროექტის ძირითადი საქაღალდის მისამართი
BASE_DIR = Path(__file__).resolve().parent


# კითხულობს მონაცემებს JSON ფაილიდან
def read_data(file_path):
    full_path = BASE_DIR / file_path

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

            # თუ ფაილი ცარიელია, აბრუნებს ცარიელ სიას
            if not content:
                return []

            # JSON ტექსტს გარდაქმნის Python მონაცემებად
            return json.loads(content)

    except FileNotFoundError:
        print(f"File not found: {full_path}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON data: {full_path}")
        return []


# წერს მონაცემებს JSON ფაილში
def write_data(file_path, data):
    full_path = BASE_DIR / file_path

    try:
        with open(full_path, "w", encoding="utf-8") as file:
            # Python მონაცემებს გარდაქმნის JSON ფორმატში
            json.dump(data, file, indent=4, ensure_ascii=False)

        return True

    except OSError as error:
        print(f"Error writing to file: {error}")
        return False
