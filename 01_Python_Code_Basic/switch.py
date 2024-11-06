def switch_case(case):
    switcher = {
        1: "Bus 1- Go to New Market",
        2: "Bus 2 - Go to Laldigir Par",
        3: "Bus 3 - Go to Agrabad",
        4: "Bus 4 - Go to University",
        5: "Bus 5 - Go to Nagirhat",
        6: "Bus 6 - Go to Rowzan",
    }

    return switcher.get(case, "Default case")

# Example usage:
case = int(input('Enter the Number: '))
result = switch_case(case)
print(result)  # Output: Case 2
