import json, sys


def load_data(filepath):
    try:
        with open(filepath) as file:
            data_list = json.load(file)
        return data_list
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def pretty_print_json(data_list):
    return json.dumps(data_list, default="Ошибка обработка данных", indent=4)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите файл с данными в качестве параметра")
        exit()

    data_list = load_data(sys.argv[1])
    if data_list is None:
        print("Невозможно обработать файл")
        exit()

    print(pretty_print_json(unformatted_json_string))
