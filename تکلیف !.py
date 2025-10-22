# ------------------------------------------
# 👨‍💻 Parsa Heidari - Python Practice
# موضوع: برعکس کردن لیست به چهار روش مختلف
# ------------------------------------------

# روش ۱️⃣ : با استفاده از Slicing
def reverse_list_slice(lst):
    """
    ورودی: لیستی از اعداد
    خروجی: نسخه‌ی برعکس‌شده از همان لیست
    روش: استفاده از برش [::-1]
    """
    return lst[::-1]


# روش ۲️⃣ : با استفاده از متد داخلی reverse()
def reverse_list_method(lst):
    """
    این متد مستقیماً لیست اصلی را تغییر می‌دهد (in-place)
    """
    lst.reverse()
    return lst


# روش ۳️⃣ : با استفاده از حلقه و insert()
def reverse_list_loop(lst):
    """
    با پیمایش لیست اصلی، هر عنصر را به ابتدای لیست جدید اضافه می‌کند
    """
    result = []
    for item in lst:
        result.insert(0, item)
    return result


# روش ۴️⃣ : با استفاده از تابع داخلی reversed()
def reverse_list_func(lst):
    """
    از تابع reversed() برای ایجاد یک iterator معکوس استفاده می‌کند،
    سپس با list() آن را به لیست تبدیل می‌کند.
    """
    return list(reversed(lst))


# ----------------------------
# 📊 بخش تست و نمایش خروجی
# ----------------------------

sample = [1, 2, 3, 4]
print("لیست اولیه:", sample)
print("---------------------------")
print("روش ۱ - Slicing:", reverse_list_slice(sample))
print("روش ۲ - reverse():", reverse_list_method(sample.copy()))
print("روش ۳ - Loop + insert:", reverse_list_loop(sample))
print("روش ۴ - reversed():", reverse_list_func(sample))
