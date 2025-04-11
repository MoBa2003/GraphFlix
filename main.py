import pandas as pd
import random

# خواندن دیتاست
df = pd.read_csv("user_movie_link.csv")  # مسیر فایل خودت رو بذار اینجا

# گروه‌بندی بر اساس userId
grouped = df.groupby("userId")

train_data = []
test_data = []

# برای هر کاربر، یکی از یال‌ها رو حذف و به داده تست منتقل کن
for user_id, group in grouped:
    if len(group) > 1:
        test_row = group.sample(n=1)
        train_rows = group.drop(test_row.index)
        test_data.append(test_row)
        train_data.append(train_rows)
    else:
        # اگر فقط یک فیلم دیده بود، نمی‌تونیم حذف کنیم، پس همه رو در train نگه می‌داریم
        train_data.append(group)

# تبدیل لیست‌ها به DataFrame
train_df = pd.concat(train_data).reset_index(drop=True)
test_df = pd.concat(test_data).reset_index(drop=True)

# ذخیره نتایج
train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)
