import subprocess,pyautogui,time
from mitmproxy import http

# ระบุที่อยู่ของโปรแกรมที่ต้องการเปิด
program_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# เรียกใช้โปรแกรม
subprocess.run(program_path)

# รอ 2 วินาทีก่อนที่จะเริ่มคลิก
time.sleep(2)

# คลิกที่พิกัด x=100 และ y=200 บนหน้าจอ
pyautogui.click(x=-1316, y=635)

