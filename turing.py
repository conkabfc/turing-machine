import turing_machine

def main():
    print('Enter a list of rules as a string - in the format\n<s,t,s,t,X>,<s,t,s,t,X>,... where s is a state, t\nis a tape symbol, and X is one of L, R, P')
    try:
        rules = turing_machine.parse_rules(input())
    except:
        print('Rules are in invalid format.')
        return
    print('Enter a list of possible states - in the format\na,b,c,d,..,z - ie each state separated by a comma')
    try:
        states = input().split(',')
    except:
        print('States are in invalid format.')
    print('Enter the starting tape, with an underscore for blanks.')
    tape = input()
    print('Enter time in ms for computation timeout')
    try:
        timeout = int(input())
    except:
        timeout = 5000
    turing_machine.turing_machine(rules, states, tape, timeout)

main()