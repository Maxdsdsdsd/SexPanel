import colorama, os, requests, ssl, time, socket, random, threading

try:
    while False:
        while True:
            exit()
            break
except:
    pass

os.system("cls||clear")

colorama.init()

def sendHexThreading(token, hex, ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 2222))
    while True:
        try:
            sock.send(bytes.fromhex(token))
            sock.recv(1024)
            time.sleep(random.uniform(0.5, 1.5))
            sock.send(bytes.fromhex(hex))
        except Exception as ex:
            print(f'Произошла ошиб-очка! {ex}')
            time.sleep(2)
            os.system("cls||clear")
            InitMain()

def onlinehack():
    _hexonline = '0000004C0A2432633536373230612D343938312D343963642D383735332D3235376539613233326630321213506C6179657252656D6F7465536572766963651A0F7365744F6E6C696E65537461747573'.lower()
    _ip = str(input("Введите айпи (БЕЗ ПОРТА!): "))
    _accounts = str(input("Введите количество аккаунтов: ")) or 1
    
    for i in range(int(_accounts)):
        _token = input(f'Введите токен ({i + 1}): ')
        my_thread = threading.Thread(target=sendHexThreading, args=(_token, _hexonline, _ip, ))
        my_thread.start()
        if i == int(_accounts):
            print("Запущено!")

def credits():
    print("Created by floppa and @BAC_TPAXAET")
    time.sleep(2)
    os.system("cls||clear")
    InitMain()

def drawMain():

    print(f'''{colorama.Fore.LIGHTBLACK_EX} 
{colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX}▄▄ {colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX} ▄▄▄ {colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX}▐▄{colorama.Fore.WHITE}•{colorama.Fore.LIGHTBLACK_EX} ▄  ▄▄▄{colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX} ▄▄▄{colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX}  ▐ ▄ ▄▄▄ {colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX}▄▄▌  
▐█ ▀{colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX} ▀▄{colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX}▀{colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX} █▌█▌{colorama.Fore.WHITE}▪{colorama.Fore.LIGHTBLACK_EX}▐█ ▄█▐█ ▀█ {colorama.Fore.WHITE}•{colorama.Fore.LIGHTBLACK_EX}█▌▐█▀▄{colorama.Fore.WHITE}.{colorama.Fore.LIGHTBLACK_EX}▀{colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX}██{colorama.Fore.WHITE}•{colorama.Fore.LIGHTBLACK_EX}
▄▀▀▀█▄▐▀▀{colorama.Fore.WHITE}▪{colorama.Fore.LIGHTBLACK_EX}▄ {colorama.Fore.WHITE}·██{colorama.Fore.WHITE}·{colorama.Fore.LIGHTBLACK_EX}  ██▀{colorama.Fore.WHITE}·▄█▀▀█ ▐█▐▐▌▐▀▀{colorama.Fore.WHITE}▪▄██{colorama.Fore.WHITE}▪  
▐█▄{colorama.Fore.WHITE}▪▐█▐█▄▄▌{colorama.Fore.WHITE}▪▐█{colorama.Fore.WHITE}·█▌▐█{colorama.Fore.WHITE}▪·•▐█ {colorama.Fore.WHITE}▪▐▌██▐█▌▐█▄▄▌▐█▌▐▌
▀▀▀▀  ▀▀▀ {colorama.Fore.WHITE}•▀▀ ▀▀{colorama.Fore.WHITE}.▀    ▀  ▀ ▀▀ █{colorama.Fore.WHITE}▪ ▀▀▀ {colorama.Fore.WHITE}.▀▀▀ 

{f'{colorama.Style.RESET_ALL}ver: 1.0'.center(42)}
    
    ''')
    print(f"{colorama.Fore.WHITE}[ Choice ]".center(44))

    print(f'''
    [ 1 ]{colorama.Fore.WHITE} —— Online Hack {colorama.Fore.LIGHTBLACK_EX}(Multiple Accounts){colorama.Style.RESET_ALL}
    [ 2 ]{colorama.Fore.WHITE} —— Credits{colorama.Style.RESET_ALL}''')

    if int(input("\n    : ")) == 1:
        onlinehack()
    else:
        credits()



def InitMain():
    drawMain()

InitMain()