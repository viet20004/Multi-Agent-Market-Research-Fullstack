import requests
import json

print("--- ĐANG KẾT NỐI ĐẾN API ---")

url = "http://127.0.0.1:8000/api/research"
payload = {"topic": "Thị phần sữa Việt Nam 2026"}

try:
    # Gửi request với stream=True để nhận dữ liệu liên tục
    response = requests.post(url, json=payload, stream=True)

    # Đọc từng dòng dữ liệu API trả về theo thời gian thực
    for line in response.iter_lines():
        if line:
            # Decode byte sang string để đọc tiếng Việt
            decoded_line = line.decode('utf-8')
            print(decoded_line)

except Exception as e:
    print(f"Lỗi kết nối: {e}")