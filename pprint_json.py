import json, sys


def load_data(filepath):
    try:
        with open(filepath) as file:
            unformatted_json_string = json.load(file)
        return unformatted_json_string
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def pretty_print_json(unformatted_json_string):
    return json.dumps(unformatted_json_string, default="Ошибка обработка данных", indent=4)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите файл с данными в качестве параметра")
        exit()

    unformatted_json_string = load_data(sys.argv[1])
    if unformatted_json_string is None:
        print("Невозможно обработать файл")
        exit()

    print(pretty_print_json(unformatted_json_string))
