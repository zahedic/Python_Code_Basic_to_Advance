def switch_case(case):
    if case == 1:
        return "Case 1"
    elif case == 2:
        return "Case 2"
    elif case == 3:
        return "Case 3"
    else:
        return "Default case"

# Example usage:
case = int(input('Enter the Number: '))
result = switch_case(case)
print(result)  # Output: Case 1
