import json, sys


def load_data(filepath):
    try:
        with open(filepath) as file:
            unformatted_data = json.load(file)
        return unformatted_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def pretty_print_json(raw_json_data):
    return json.dumps(raw_json_data, default="Ошибка обработка данных", indent=4)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите файл с данными в качестве параметра")
        exit()

    unformatted_data = load_data(sys.argv[1])
    if unformatted_data is None:
        print("Невозможно обработать файл")
        exit()

    print(pretty_print_json(unformatted_data))
