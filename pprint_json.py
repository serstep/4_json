import json, sys


def load_data(filepath):
    try:
        raw_json_data = ""
        with open(filepath) as file:
            raw_json_data = json.load(file)
        return raw_json_data
    except:
        return None


def pretty_print_json(raw_json_data):
    return json.dumps(raw_json_data, default="Ошибка обработка данных", indent=4)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите файл с данными в качестве параметра")
        exit()

    formatted_data = load_data(sys.argv[1])
    if formatted_data is None:
        print("Невозможно оработать файл")
        exit()

    print(pretty_print_json(formatted_data))
