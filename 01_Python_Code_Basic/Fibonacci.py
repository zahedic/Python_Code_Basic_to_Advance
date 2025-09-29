def fibonacci(n):
    if n == 0:  # বেস কেস
        return 0
    elif n == 1:  # বেস কেস
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # রিকারসিভ কেস

# ব্যবহার
num = 5
print(f"Fibonacci of {num} is {fibonacci(num)}")  # আউটপুট: 8
