def factorial(n):
    if n == 0:  # বেস কেস
        return 1
    else:
        return n * factorial(n - 1)  # রিকারসিভ কেস

# ব্যবহার
print(factorial(998))  # আউটপুট: 120
