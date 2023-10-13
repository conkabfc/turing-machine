def turing_machine(rules, states, tape, timeout):
    tape_array = [char for char in tape]
    tape_len = len(tape_array)
    head_ind = 0
    curr_state = states[0]
    if tape_len == 0:
        tape_array = ['_']

    while curr_state != states[1]:
        try:
            curr_sym = tape_array[head_ind]
            rule = rules[curr_state][curr_sym]
            curr_state = rule[0]
            tape_array[head_ind] = rule[1]
            if rule[2] == 'L':
                if head_ind == 0:
                    tape_array = ['_']*5 + tape_array
                    head_ind += 5 # 5 new elements
                    tape_len += 5
                head_ind -= 1
            elif rule[2] == 'R':
                if head_ind == (tape_len - 1):
                    tape_array += ['_']*5 + tape_array
                head_ind += 1
        except:
            print("HALT IN NON-ACCEPT STATE")
            break
    if curr_state == states[1]:
        print("HALT IN ACCEPT STATE")

    return 0

def parse_rules(rule_str):
    rule_str = rule_str[1:-1].split('>,<')
    rule_dict = {}
    for rule in rule_str:
        rule_split = rule.split(',')
        if rule_split[0] not in rule_dict:
            rule_dict[rule_split[0]] = {rule_split[1] : rule_split[2:5]}
        else:
            if rule_split[1] not in rule_dict[rule_split[0]]:
                rule_dict[rule_split[0]][rule_split[1]] = rule_split[2:5]
            else:
                rule_dict[rule_split[0]][rule_split[1]].append(rule_split[2:5])
    return rule_dict