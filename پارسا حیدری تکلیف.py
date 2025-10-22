"Salam   kh  ob   has  tin?"
text = input("Enter a sentence: ")

result = ""          # رشته‌ی نهایی که می‌سازیم
previous_char = ""   # برای بررسی کاراکتر قبلی

for char in text:
    # فقط وقتی کاراکتر فعلی space هست و قبلی هم space بوده، ردش کن
    if char == " " and previous_char == " ":
        continue
    # در غیر این صورت، اضافه‌اش کن به نتیجه
    result += char
    previous_char = char

print(result)
