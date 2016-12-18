import json, sys


def load_data(filepath):
    try:
        data = ""
        with open(filepath) as file:
            data = json.load(file)
        return data
    except:
        return None


def pretty_print_json(data):
    return json.dumps(data, default="Ошибка обработка данных", indent=4)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите файл с данными в качестве параметра")
        exit()

    data = load_data(sys.argv[1])
    if data is None:
        print("Невозможно оработать файл")
        exit()

    print(pretty_print_json(data))
