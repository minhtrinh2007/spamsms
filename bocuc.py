
import sys
import requests
def logo():
    print("")
    print('███╗   ███╗████████╗  ████████╗ █████╗  █████╗ ██╗     ')
    print('███╗   ███╗████████╗  ████████╗ █████╗  █████╗ ██╗     ')
    print('████╗ ████║╚══██╔══╝  ╚══██╔══╝██╔══██╗██╔══██╗██║     ')
    print('██╔████╔██║   ██║        ██║   ██║  ██║██║  ██║██║     ')
    print('██║╚██╔╝██║   ██║        ██║   ██║  ██║██║  ██║██║    ')
    print('██║ ╚═╝ ██║   ██║        ██║   ╚█████╔╝╚█████╔╝███████╗')
    print('╚═╝     ╚═╝   ╚═╝        ╚═╝    ╚════╝  ╚════╝ ╚══════╝')
    print('Tool spam sms by MT TOOL')
    print('Liên hệ Telegram @ncgb nếu xảy ra lỗi')
    print('Liên hệ Telegram @ncgb mua gói VIP')
    print('---------------------------------------------------------')
logo()

def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)
          # In thông báo nếu thành công
        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: không có internet")  # In thông báo lỗi nếu xảy ra lỗi
        sys.exit()  # Thoát chương trình nếu có lỗi

# Gọi hàm lấy thông tin vị trí
city, region, country, latitude, longitude = get_location_by_ip()


#API KEY

