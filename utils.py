from req_and_res import get_json, post_json


def initializing_components(*components):
    for component in components:
        component.pack()


def get_values_components(url, method):
    components_values_dict = {}

    components_values_dict["url"] = url.get()
    components_values_dict["method"] = method.get()

    return components_values_dict


def options_send_button(url="", method="GET", json={}):
    if method == "GET":
        get_json(url)
    elif method == "POST":
        post_json(url, json)
    else:
        print("QUE!!??")


def send_request_button(url, method, json={"hola": "hola"}):
    components = get_values_components(url, method)

    options_send_button(components["url"], components["method"], json)
