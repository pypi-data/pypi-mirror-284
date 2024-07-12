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


def rule_to_dict(rules, curr=0):
    is_rule = rules[curr][0]
    if is_rule:
        _, feat_list, coef_list, thr, cat, _ = rules[curr]
        node_l, dict_l = rule_to_dict(rules, curr + 1)
        node_r, dict_r = rule_to_dict(rules, curr + node_l + 1)

        return node_l + node_r + 1, {
            "is_rule": is_rule,
            "feat_list": feat_list,
            "coef_list": coef_list,
            "thr": thr,
            "cat": cat,

            "left": dict_l,
            "right": dict_r
        }
    else:
        _, label, samples, support, _ = rules[curr]
        return 1, {
            "is_rule": is_rule,
            "label": label,
            "samples": samples,
            "support": support,
        }


def plot_dec_bounds(rules, plt, x_min=None, x_max=None, y_min=None, y_max=None):
    if x_min is None:
        _, rules = rule_to_dict(rules)
        x_min, x_max = plt.xlim()
        y_min, y_max = plt.ylim()
        for x, y in plot_dec_bounds(rules, plt, x_min, x_max, y_min, y_max):
            plt.plot(x, y)
    elif rules["is_rule"]:
        thr = rules["thr"]
        l = rules["left"]
        r = rules["right"]

        if 0 == rules["feat_list"][0]:  # 0 = x
            return [[(thr, thr), (y_min, y_max)]] + \
                plot_dec_bounds(l, plt, x_min, thr, y_min, y_max) + \
                plot_dec_bounds(r, plt, thr, x_max, y_min, y_max)
        else:
            thr = rules["thr"]
            l = rules["left"]
            r = rules["right"]
            return [[(x_min, x_max), (thr, thr)]] + \
                plot_dec_bounds(l, plt, x_min, x_max, y_min, thr) + \
                plot_dec_bounds(r, plt, x_min, x_max, thr, y_max)
    return []
