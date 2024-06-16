import os
import sys
import time
import requests
import smtplib

'''
Foreground colors:

Black: \033[30m or \033[0;30m
Red: \033[31m or \033[0;31m
Green: \033[32m or \033[0;32m
Yellow: \033[33m or \033[0;33m
Blue: \033[34m or \033[0;34m
Magenta: \033[35m or \033[0;35m
Cyan: \033[36m or \033[0;36m
White: \033[37m or \033[0;37m

Background colors:

Black: \033[40m
Red: \033[41m
Green: \033[42m
Yellow: \033[43m
Blue: \033[44m
Magenta: \033[45m
Cyan: \033[46m
White: \033[47m

Text effects:

Bold: \033[1m
Underline: \033[4m
Blink: \033[5m
Reverse: \033[7m
'''

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
M = '\033[0;35m'
BOLD = '\033[1m'


def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)


def ascii_loading_animation(line_length=10, duration=2, interval=0.1):
    num_iterations = int(duration / interval)
    for i in range(num_iterations):
        sys.stdout.write("=" * line_length + f'{i*5}%')
        sys.stdout.write("\b" * line_length)  # Move cursor back
        sys.stdout.flush()
        time.sleep(interval)

    # Clear the line
    sys.stdout.write(" " * line_length)
    sys.stdout.write("\b" * line_length)
    sys.stdout.flush()


def check_internet_connection():
    try:
        res = requests.get('http://google.com')
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def clear_screen():
    os.system("clear")


def print_logo():
    logo = """
    \033[1;33m  __  __       _ _             ___    ___
    \033[1;33m |  \/  |     (_) |            |  \  /  |
    \033[1;33m | \  / | __ _ _| | ___ _ __    |  \/  |
    \033[1;33m | |\/| |/ _  | | |/ _ \  __|    |    |
    \033[1;33m | |  | | (_| | | |  __/ |      |  /\  |
    \033[1;33m |_|  |_|\__,_|_|_|\___|_|     |__/  \__|
    
    \033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY SK MIRAJ \033[1;31m(\033[1;33mSK PRODUCTION\033[1;31m) 
    """
    print(logo)


def send_mail():
    nameVictim = input(G + ' Enter reciver Name ' + C + " : " + Y)
    to_id = input(G + " Enter reciver Email " + C + " : " + Y)
    subject = input(G + " Input Mail Subject" + C + " : " + Y)
    msg_content = input(G + " Input Mail Content" + C + " : " + Y)

    GMAIL_ID = "skmirajulislam181@gmail.com"
    GMAIL_PSD = "ykqd tybo cbps egml"

    to = to_id
    sub = f"{subject}"
    msg = f"Dear {nameVictim}'\n\n {msg_content} \n\n Best regards, sk miraj"

    def send():
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        try:
            s.login(GMAIL_ID, GMAIL_PSD)
            s.sendmail("your name", to, f"subject: {sub} \n\n {msg}")
        except Exception as e:
            print(R+" Unwanted error occurred!! : " + str(e))
            sys.exit()  # Stop execution if an error occurs
        s.quit()
    send()


def main():
    clear_screen()
    print_logo()
    print('')
    if check_internet_connection():
        send_mail()
        hprint(G + " Sending Email .........")
        time.sleep(2)
        hprint(G+" Email successfully sent to reciver !")
        time.sleep(2)
        hprint(G + " Process can take some time !")
    else:
        hprint(" No internet connection [!]")
        sys.exit()


if __name__ == "__main__":
    hprint(C + "Launching Mailer X...")
    ascii_loading_animation()
    main()
