def case_1():
    return "Department of ICT"

def case_2():
    return "Department of Mathematics"

def case_3():
    return "Department of AI & Machine Learning Engineering."

def default_case():
    return "Department of Applied Physics"

def switch_case(case):
    switcher = {
        1: case_1,
        2: case_2,
        3: case_3
    }
    # Call the function from the dictionary. If the case does not exist, call the default function.
    return switcher.get(case, default_case)()

# Example usage:
case = int(input('Enter the Number: '))
result = switch_case(case)
print(result)  # Output: Executing case 3
