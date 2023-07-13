import requests


def get_info_from_api(url):
    response = requests.get(url)
    data = response.json()
    return data


def get_count_austronauts(data):
    return data["number"]


def get_list_austronauts(data):
    list_astro = []
    for a in data["people"]:
        craft = a["craft"]
        name_astro = a["name"]
        list_astro.append(f"{craft} {name_astro}")
    return list_astro


def print_info_from_api(data):
    print_info_from_api_count_astro(data)
    print_list_austronauts(data)


def print_info_from_api_count_astro(data):
    print(f"Now we have {get_count_austronauts(data)} austronauts in space")


def print_list_austronauts(data):
    for count, astro in enumerate(get_list_austronauts(data)):
        print(count + 1, astro)
