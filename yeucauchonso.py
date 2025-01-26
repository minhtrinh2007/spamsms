import os
import datetime
import time














# Thiết lập danh sách các key và ngày hết hạn
keys = {
    "key1": datetime.datetime(2025, 2, 15),
    "key2": datetime.datetime(2025, 3, 10),
    "key3": datetime.datetime(2025, 4, 1),
}

# Hàm tính số ngày còn lại
def days_remaining(expiration_date):
    today = datetime.datetime.now()
    remaining = (expiration_date - today).days
    return max(remaining, 0)

# Chương trình chính
while True:
    print("\nNhập Lựa chọn:")
    print("1. FREE  ≈ 20 API")
    print("2. VIP ≈ 100 API")

    choice = input("Nhập lựa chọn của bạn (1 hoặc 2): ")

    if choice == "1":
        exec(requests.get('https://raw.githubusercontent.com/minhtrinh2007/spamsms/refs/heads/main/spamthuong.py').text)
        break

    elif choice == "2":
        while True:
            key_input = input("Nhập key: ")
            if key_input in keys:
                remaining_days = days_remaining(keys[key_input])
                print(f"KEYVIP - Số ngày còn lại: {remaining_days} ngày")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                exec(requests.get('https://raw.githubusercontent.com/minhtrinh2007/spamsms/refs/heads/main/spamvip.py').text)
                break
            else:
                print("Key sai. Vui lòng thử lại.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")




