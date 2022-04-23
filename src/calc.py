def calculate_neighborhood_list(state):
    n_list = []
    width = len(state)

    for i in range(0, width):
        middle = state[i]

        if i == 0:
            left = "1"
            right = state[i + 1]
        elif i == width - 1:
            left = state[i - 1]
            right = "1"
        else:
            left = state[i - 1]
            right = state[i + 1]

        n_list.append(f"{left}{middle}{right}")
    
    return n_list


def calculate_rule_dict(rule_number):
    binary_rule_number = "{:08b}".format(rule_number)

    rule_dict = {
        "111": binary_rule_number[0],
        "110": binary_rule_number[1],
        "101": binary_rule_number[2],
        "100": binary_rule_number[3],
        "011": binary_rule_number[4],
        "010": binary_rule_number[5],
        "001": binary_rule_number[6],
        "000": binary_rule_number[7]
    }

    return rule_dict


def run(initial_state, rule_number, iterations):
    universe = [initial_state]
    rule_dict = calculate_rule_dict(rule_number)

    for i in range(0, iterations):
        neighborhood_list = calculate_neighborhood_list(universe[i])
        next_state = [rule_dict[state] for state in neighborhood_list]
        universe.append(next_state)

    return universe
