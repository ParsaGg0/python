# --------------------------------------
# 👨‍💻 Parsa Heidari - تمرین نجات شهر
# موضوع: یافتن زیرمجموعه‌هایی که جمع‌شان عدد اول است
# --------------------------------------

from itertools import combinations

# تابع بررسی عدد اول
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# تابع اصلی برای یافتن ترکیب‌های معتبر
def rescue_city(tokens):
    valid_combos = []
    for r in range(1, len(tokens) + 1):  # از زیرمجموعه‌های 1 عضوی تا n عضوی
        for combo in combinations(tokens, r):
            if is_prime(sum(combo)):
                valid_combos.append(combo)
    return valid_combos


# ---------------------------
# 🧪 بخش تست
# ---------------------------
tokens = [2, 3, 5, 8]
result = rescue_city(tokens)

print("توکن‌ها:", tokens)
print("زیرمجموعه‌های نجات‌دهنده:")
for combo in result:
    print(combo, "→ جمع:", sum(combo))
