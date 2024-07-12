import json


def eval_node(node):
    if type(node) is list:
        return [eval_node(el) for el in node]
    else:
        value_type = node["type"]
        value = node["value"]

        if value_type in ('bool', 'bool_'):
            value = value == 'True'
        elif value_type in ('int', 'longlong', 'int64'):
            value = int(value)
        elif value_type in ('float', 'float64'):
            value = float(value)
        else:
            value = value

        return value


def eval_response(res_txt):
    res = json.loads(res_txt)

    return_value = {
        "labels": [int(x) for x in res["labels"]],
        "rules": []
    }

    for rule_node in res["rules"]:
        return_value["rules"].append(eval_node(rule_node))

    return return_value
