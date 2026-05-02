import json
import sys

if len(sys.argv) != 4:
    print(f"Программа сработает только с 3-мя параметрами "
          "\n запуск: python task3.py tests.json values.json report.json")

    sys.exit(1)

tests = sys.argv[1]
values_file = sys.argv[2]
report = sys.argv[3]

with open(tests, 'r') as f:
    test_dict = json.load(f)

with open(values_file, 'r') as f:
    file_value = json.load(f)

updates = {}
for item in file_value.get("values", []):
    updates[item['id']] = item['value']

result_list = [test_dict]

while result_list:
    current = result_list.pop()

    if isinstance(current, dict):
        if "id" in current and current["id"] in updates:
            current["value"] = updates[current["id"]]

        for value in current.values():
            result_list.append(value)

    elif isinstance(current, list):
        for item in current:
            result_list.append(item)

with open(report, "w") as f:
    json.dump(test_dict, f, indent=4)