def turing_machine(rules, states, tape, timeout):
    return 0

def parse_rules(rule_str):
    rule_str = rule_str[1:-1].split('>,<')
    rule_dict = {}
    for rule in rule_str:
        rule_split = rule.split(',')
        if rule_split[0] not in rule_dict:
            rule_dict[rule_split[0]] = {rule_split[1] : [rule_split[2:5]]}
        else:
            if rule_split[1] not in rule_dict[rule_split[0]]:
                rule_dict[rule_split[0]][rule_split[1]] = [rule_split[2:5]]
            else:
                rule_dict[rule_split[0]][rule_split[1]].append(rule_split[2:5])
    return rule_dict