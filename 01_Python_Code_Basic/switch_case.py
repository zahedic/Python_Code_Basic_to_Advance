def switch_case(case):
    match case:
        case 1:
            return "Case 1"
        case 2:
            return "Case 2"
        case 3:
            return "Case 3"
        case _:
            return "Default case"

# Example usage:
case = int(input('Enter the Number: '))
result = switch_case(case)
print(result)  # Output: Case 2

