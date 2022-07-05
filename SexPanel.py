import os, socket, threading, time, sys, base64
tt = '00:00:00'
s = 0
mn = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "55", "0", "00", "000"]
lm = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "0"]
km = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "0"]
omm = ["1", "2", "3", "4", "5", "0"]
ku1227 = base64.b64decode('CiAg4paI4paI4paI4paI4paI4paIIOKWk+KWiOKWiOKWiOKWiOKWiCDilpLilojiloggICDilojilojilpIg4paI4paI4paT4paI4paI4paIICAg4paE4paE4paEICAgICAgIOKWiOKWiOKWiOKWhCAgICDilogg4paT4paI4paI4paI4paI4paIICDilojilojilpMgICAgCuKWkuKWiOKWiCAgICDilpIg4paT4paIICAg4paAIOKWkuKWkiDilogg4paIIOKWkuKWkeKWk+KWiOKWiOKWkSAg4paI4paI4paS4paS4paI4paI4paI4paI4paEICAgICDilojilogg4paA4paIICAg4paIIOKWk+KWiCAgIOKWgCDilpPilojilojilpIgICAgCuKWkSDilpPilojilojiloQgICDilpLilojilojiloggICDilpHilpEgIOKWiCAgIOKWkeKWk+KWiOKWiOKWkSDilojilojilpPilpLilpLilojiloggIOKWgOKWiOKWhCAg4paT4paI4paIICDiloDilogg4paI4paI4paS4paS4paI4paI4paIICAg4paS4paI4paI4paRICAgIAogIOKWkiAgIOKWiOKWiOKWkuKWkuKWk+KWiCAg4paEICDilpEg4paIIOKWiCDilpIg4paS4paI4paI4paE4paI4paT4paSIOKWkuKWkeKWiOKWiOKWhOKWhOKWhOKWhOKWiOKWiCDilpPilojilojilpIgIOKWkOKWjOKWiOKWiOKWkuKWkuKWk+KWiCAg4paEIOKWkuKWiOKWiOKWkSAgICAK4paS4paI4paI4paI4paI4paI4paI4paS4paS4paR4paS4paI4paI4paI4paI4paS4paS4paI4paI4paSIOKWkuKWiOKWiOKWkuKWkuKWiOKWiOKWkiDilpEgIOKWkSDilpPiloggICDilpPilojilojilpLilpLilojilojilpEgICDilpPilojilojilpHilpHilpLilojilojilojilojilpLilpHilojilojilojilojilojilojilpIK4paSIOKWkuKWk+KWkiDilpIg4paR4paR4paRIOKWkuKWkSDilpHilpLilpIg4paRIOKWkeKWkyDilpHilpLilpPilpLilpEg4paRICDilpEg4paS4paSICAg4paT4paS4paI4paR4paRIOKWkuKWkSAgIOKWkiDilpIg4paR4paRIOKWkuKWkSDilpHilpEg4paS4paR4paTICDilpEK4paRIOKWkeKWkiAg4paRIOKWkSDilpEg4paRICDilpHilpHilpEgICDilpHilpIg4paR4paR4paSIOKWkSAgICAgICDilpIgICDilpLilpIg4paR4paRIOKWkeKWkSAgIOKWkSDilpLilpEg4paRIOKWkSAg4paR4paRIOKWkSDilpIgIOKWkQrilpEgIOKWkSAg4paRICAgICDilpEgICAg4paRICAgIOKWkSAg4paR4paRICAgICAgICAg4paRICAg4paSICAgICAg4paRICAg4paRIOKWkSAgICDilpEgICAgIOKWkSDilpEgICAKICAgICAg4paRICAgICDilpEgIOKWkSDilpEgICAg4paRICAgICAgICAgICAgICAgICDilpEgIOKWkSAgICAgICAgIOKWkSAgICDilpEgIOKWkSAgICDilpEgIOKWkQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiBBdXRob3JzOiAKIFNvdXJjZTogaVBhZmYgQGNyZWF0aGV4IAogSGV4ZXMgYnkgQG5pa2thYmVzdFxu').decode('utf-8')

def banner():
    os.system('cls||clear')
    print(ku1227)


def times():
    global s
    global tt
    while 1:
        time.sleep(1)
        s += 1
        h = s // 60 // 60
        mm = s // 60 - h*0
        ss = s - h*60*60 - mm*60
        tt = (f'{h:02}:{mm:02}:{ss:02}')

def menu():
    from config import ip, token, name
    global s, ip, token
    banner()
    print("          Приветсвую вас, {}!".format(name))
    time.sleep(1)
    banner()
    print("          >Created by t.me/CreatHex<")
    print(" [1] Сustom hex \n [2] Ban wish 1005 \n [3] Medal 2021 menu \n [4] KD menu \n [5] Unvisible NickName \n [6] lvl menu  \n [7] piar channel NickName \n [8] Unlimited online account \n [9] 1800xp \n [10] Exchange 10Gold to 100Silver \n\n>[0] Edit iP \n>[00] Edit Token \n>[000] Check Token \n>>[55 = exit, CTRL + Z = Crach]")
    choice = input(" >> ")
    while choice not in mn:
        print(" Invalid input numbers")
        time.sleep(0.5)
        banner()
        print("            >Created by t.me/CreatHex<")
        print(" [1] Сustom hex \n [2] Ban wish 1005 \n [3] Medal 2021 menu \n [4] KD menu (Risk ban) \n [5] Unvisible NickName \n [6] lvl menu (Risk ban) \n [7] Piar channel nickname \n [8] Unlimited online account \n [9] 1800 xp  \n [10] Exchange 10Gold to 100Silver \n\n>[0] Edit iP \n>[00] Edit Token \n>[000] Check Token \n>>[55 = exit, CTRL + Z = Crach]")
        choice = input(" >> ")

    if choice == "0":
        banner()
        print("                  >Set new cfg<")
        ip = input(" Enter new iP >> ")
        with open('config.py', 'w') as f:pass
        with open('config.py', 'w') as f:
            f.write(f'ip = "{ip}"')
            f.close()
        from config import ip, token, name
        menu()

    if choice == "00":
        banner()
        print("              >Set new cfg<")
        token = input("Enter new Token >> ")
        with open('config.py', 'w') as f:pass
        with open('config.py', 'w') as f:
            f.write(f'token = "{token}"')
            f.close()
        from config import ip, token, name
        menu()

    if choice == "000":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 2222))
        s.send(bytes.fromhex(token))
        o = s.recv(1024).decode("utf-8", errors="ignore")
        if o[3] == '(':
            s.close()
        else:
            banner()
            print("            token invalid! Pls change token")
            time.sleep(2)
            menu()

    if choice == "1":
        banner()
        print(">When using third-party Hex, chance of a ban is more<")
        hex = input(" Enter your Hex >> ")        
        sendhex(ip, token, hex)

    if choice == "2":
        sendhex(ip, token, '000000b00a2433363038393761342d396538392d343261642d616362652d6233666364633836633930651213506c6179657252656d6f7465536572766963651a0d736574506c617965724e616d6522641a620a60e180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aae180aa2262792059616b6173616d6922')

    if choice == "3":
        banner()
        print("  >No type in chat if you use no in order<")
        print("            >Say thx only me<")
        print(">>Medal 21 years dup\n [1] Bronze medal \n [2] Silver medal \n [3] Gold medal \n [4] Platinum medal \n [5] DIAMOND medal \n\n [0] Exit to menu")
        choice_omm = input(" >> ")
        while choice_omm not in omm:
            print(" Invalid input numbers")
            time.sleep(0.5)
            banner()
            print("  >No type in chat if you use no in order<")
            print("            >Say thx only me<")
            print("\n>>Medal 21 years dup\n [1] Bronze medal \n [2] Silver medal \n [3] Gold medal \n [4] Platinum medal \n [5] DIAMOND medal \n\n [0] Exit to menu")
            choice_omm = input(" >> ")

        if choice_omm == "0":
            menu()

        if choice_omm == "1":
            sendhex(ip, token, '000000760a2463333632373838362d373762622d346539612d623931642d3162646438396561663363321216496e76656e746f727952656d6f7465536572766963651a0d6578656375746552656369706522231a210a1f5245434950455f4d4544414c5f5645544552414e323032315f42524f4e5a4522002200')

        if choice_omm == "2":
            sendhex(ip, token, '0000007b0a2438343439343663392d666637612d346631332d393433312d3062306435643236653763371216496e76656e746f727952656d6f7465536572766963651a0d6578656375746552656369706522231a210a1f5245434950455f4d4544414c5f5645544552414e323032315f53494c564552220022051a030a0102')
        
        if choice_omm == "3":
            sendhex(ip, token, '000000790a2433353235376232352d616232612d343233642d386465302d6331376665373462633465331216496e76656e746f727952656d6f7465536572766963651a0d6578656375746552656369706522211a1f0a1d5245434950455f4d4544414c5f5645544552414e323032315f474f4c44220022051a030a0102')
            
        if choice_omm == "4":
            sendhex(ip, token, '0000007d0a2439323934316632322d393538372d343239332d616335642d3737353461636263393431661216496e76656e746f727952656d6f7465536572766963651a0d6578656375746552656369706522251a230a215245434950455f4d4544414c5f5645544552414e323032315f504c4154494e554d220022051a030a0102')
                  
        if choice_omm == "5":
            sendhex(ip, token, '0000007c0a2430343033303435642d616435312d343236352d613838352d3033333462663162353264611216496e76656e746f727952656d6f7465536572766963651a0d6578656375746552656369706522241a220a205245434950455f4d4544414c5f5645544552414e323032315f4449414d4f4e44220022051a030a0102')

    if choice == "4":
        banner()
        print("         >All hexes here by @nikkabest lel<")
        print("       >Maybe ban idk<")
        print(">>KD Menu \n [1] General 1.58 \n [2] Clear KD \n [3] Cheat KD \n   \n\n [0] Exit to menu")
        choice_km = input(" >> ")
        while choice_km not in km:
            print(" Invalid input numbers")
            time.sleep(0.5)
            banner()
            print("         >@flopkachan<")
            print("       >You use category high risk<")
            print(">>KD Menu \n [1] General 1.58 \n [2] Clear stats \n [3] Cheat KD \n [0] Exit to menu")
            choice_km = input(" >> ")
            
        if choice_km == "0":
            menu()
            
        if choice_km == "1":
            sendhex(ip, token, '000002fa0a2432386539333461642d366264392d343163632d386165312d3834656533303165616337321218506c61796572537461747352656d6f7465536572766963651a0a73746f7265537461747322a90512160a1064656174686d617463685f73686f7473108c844b12200a1a67756e5f64656174686d617463685f616b7231325f73686f747310e8bd0612150a0f64656174686d617463685f6869747310b8850a121e0a1967756e5f64656174686d617463685f616b7231325f6869747310966c12180a1164656174686d617463685f64616d616765109d80a40412210a1b67756e5f64656174686d617463685f616b7231325f64616d61676510f8a02712170a1164656174686d617463685f64656174687310928f0212160a1064656174686d617463685f6b696c6c7310cff603121f0a1a67756e5f64656174686d617463685f616b7231325f6b696c6c73109b28121a0a1464656174686d617463685f6865616473686f747310fe890212230a1e67756e5f64656174686d617463685f616b7231325f6865616473686f747310d01b12170a1264656174686d617463685f61737369737473108246121e0a1867756e5f64656174686d617463685f61776d5f73686f747310adb902121c0a1767756e5f64656174686d617463685f61776d5f6869747310975f121f0a1967756e5f64656174686d617463685f61776d5f64616d61676510fbf977121d0a1867756e5f64656174686d617463685f61776d5f6b696c6c7310eb58121e0a1867756e5f64656174686d617463685f616b725f73686f7473109eb11e121d0a1767756e5f64656174686d617463685f616b725f6869747310bfcc0312200a1967756e5f64656174686d617463685f616b725f64616d61676510cfa4ae01121e0a1867756e5f64656174686d617463685f616b725f6b696c6c7310d4ab0112210a1c67756e5f64656174686d617463685f616b725f6865616473686f747310e26e120d0a086c6576656c5f7870108e05121c0a1764656174686d617463685f67616d65735f706c6179656410b90e2200')
            
        if choice_km == "2":
            sendhex(ip, token, '000002350a2437366232323666322d616637372d346661622d383438392d3066626335623739366665611218506c61796572537461747352656d6f7465536572766963651a0a73746f7265537461747322e40312110a0c6465667573655f73686f747310810112180a1467756e5f6465667573655f616b725f73686f7473101212110a0d6465667573655f6465617468731007121b0a1767756e5f6465667573655f736d313031345f73686f7473100212180a1467756e5f6465667573655f6732325f73686f7473102812180a1467756e5f6465667573655f61776d5f73686f74731012120f0a0b6465667573655f68697473100212170a1367756e5f6465667573655f61776d5f68697473100112120a0d6465667573655f64616d61676510be0112190a1567756e5f6465667573655f61776d5f64616d616765105612100a0c6465667573655f6b696c6c73100212180a1467756e5f6465667573655f61776d5f6b696c6c731001121a0a1667756e5f6465667573655f616b7231325f73686f7473103312190a1567756e5f6465667573655f616b7231325f686974731001121b0a1767756e5f6465667573655f616b7231325f64616d6167651068121a0a1667756e5f6465667573655f616b7231325f6b696c6c73100112140a106465667573655f6865616473686f74731001121e0a1a67756e5f6465667573655f616b7231325f6865616473686f74731001120d0a086c6576656c5f787010960112170a136465667573655f67616d65735f706c6179656410022200')
            
        if choice_km == "3":
            sendhex(ip, token, '0000030a0a2439636266633337312d646239382d343131362d616232332d3463356463343739353432371218506c61796572537461747352656d6f7465536572766963651a0a73746f7265537461747322b90512110a0c6465667573655f73686f747310850d121b0a1767756e5f6465667573655f646561676c655f73686f7473100e121b0a1667756e5f6465667573655f66616d61735f73686f747310960112100a0b6465667573655f6869747310c90112190a1567756e5f6465667573655f66616d61735f68697473101712130a0d6465667573655f64616d61676510f78e01121c0a1767756e5f6465667573655f66616d61735f64616d61676510f90612100a0c6465667573655f6b696c6c731053121a0a1667756e5f6465667573655f66616d61735f6b696c6c73100612140a106465667573655f6865616473686f74731040121e0a1a67756e5f6465667573655f66616d61735f6865616473686f7473100412110a0d6465667573655f646561746873100e12120a0e6465667573655f61737369737473100412190a1467756e5f6465667573655f6d31365f73686f7473109d0212170a1367756e5f6465667573655f6d31365f68697473101c121a0a1567756e5f6465667573655f6d31365f64616d61676510b50712180a1467756e5f6465667573655f6d31365f6b696c6c731009121c0a1867756e5f6465667573655f6d31365f6865616473686f7473100312190a1567756e5f6465667573655f6d3461315f73686f7473101a12180a1467756e5f6465667573655f6d3461315f686974731005121b0a1667756e5f6465667573655f6d3461315f64616d61676510bb0112190a1567756e5f6465667573655f6d3461315f6b696c6c731001121d0a1967756e5f6465667573655f6d3461315f6865616473686f74731001121a0a1667756e5f6465667573655f616b7231325f73686f7473101112190a1467756e5f6465667573655f61776d5f73686f7473108f03120d0a086c6576656c5f787010d505120c0a086c6576656c5f6964100212170a136465667573655f67616d65735f706c6179656410062200')
        
        
        

    if choice == "6":
        banner()
        print("   >@flopkachan")
        print("        >You use category high risk<")
        print(">>Lvl menu:\n [1] 11 lvl \n [2] 16 lvl \n [0] Exit to menu")
        choice_lm = input(" >> ")
        while choice_lm not in lm:
            print(" Invalid input numbers")
            time.slepp(0.5)
            banner()
            print("   @flopkachan")
            print("        >You use category high risk<")
            print(">>Lvl menu:\n [1] 11 lvl \n [2] 16 lvl \n  [0] Exit to menu")
            choice_lm = input(" >> ")
        
        if choice_lm == "0":
            menu()

        if choice_lm == "1":
            sendhex(ip, token, '0000027b0a2430306636346139372d313765612d346266312d626165642d3262653565363734306533311218506c61796572537461747352656d6f7465536572766963651a0a73746f7265537461747322aa0412160a1064656174686d617463685f73686f747310abab0112200a1a67756e5f64656174686d617463685f616b7231325f73686f747310b3d00612140a0f64656174686d617463685f6869747310de15121e0a1967756e5f64656174686d617463685f616b7231325f68697473109b6d12170a1164656174686d617463685f64616d61676510ea9b1012210a1b67756e5f64656174686d617463685f616b7231325f64616d6167651091e32712150a1064656174686d617463685f6b696c6c7310dd0a121f0a1a67756e5f64656174686d617463685f616b7231325f6b696c6c7310d92812190a1464656174686d617463685f6865616473686f747310cd0812230a1e67756e5f64656174686d617463685f616b7231325f6865616473686f747310831c12160a1164656174686d617463685f64656174687310cd0412160a1264656174686d617463685f617373697374731079121d0a1867756e5f64656174686d617463685f6d31365f73686f747310ec02121b0a1767756e5f64656174686d617463685f6d31365f686974731032121e0a1967756e5f64656174686d617463685f6d31365f64616d61676510be0f121c0a1867756e5f64656174686d617463685f6d31365f6b696c6c73101112200a1c67756e5f64656174686d617463685f6d31365f6865616473686f74731007120d0a086c6576656c5f787010a602120c0a086c6576656c5f6964100a121b0a1764656174686d617463685f67616d65735f706c61796564102f2200')
            
        if choice_lm == "2":
            sendhex(ip, token, '000000c60a2433316535323265382d386363332d346365612d626334642d6665633739653037303364361218506c61796572537461747352656d6f7465536572766963651a0a73746f72655374617473227612110a0d6465667573655f646561746873106312110a0c6465667573655f73686f747310d37a12180a1467756e5f6465667573655f6732325f73686f74731006120d0a086c6576656c5f787010b702120c0a086c6576656c5f6964100f12170a136465667573655f67616d65735f706c6179656410162200')
            

    if choice == "7":
        sendhex(ip, token, '0000005B0A2433353564333336322D336638332D346566312D623033622D6232313330663666353831621213506C6179657252656D6F7465536572766963651A0D736574506C617965724E616D65220F1A0D0A0B746720666c6f706b616368616e')

    if choice == "8":
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, 2222))
        except:
            banner()
            sys.exit("\nFailed to connect to Standoff 2 server. \n Try changing the server iP!")
        x = threading.Thread(target=times, daemon=True)
        banner()
        print("   Dup is started! [ CTRL + Z - Crach! ]")
        time.sleep(0.5)
        i = 0
        x.start()
        while 4:
            try:
                i += 1
                time.sleep(0.01)
                sock.send(bytes.fromhex(token))
                sock.send(bytes.fromhex('000000530a2462623634303038352d346635392d343235342d613130302d30666230343165623631393012184d617463686d616b696e6752656d6f7465536572766963651a11676574496e7669746573546f4c6f626279'))
                print(f' {i} - Packets |  {tt}  |  [ CTRL + Z - Crach ]\n bruh(lel) what changed ? added (trying) antiban')
            except:
                sock.connect((ip, 2222))

    if choice == "9":
        sendhex(ip, token,'0000006d0a2439333263373866312d306361322d343462622d393438622d3535623330616632336261301218506c61796572537461747352656d6f7465536572766963651a0a73746f72655374617473221d120d0a086c6576656c5f7870108b03120c0a086c6576656c5f6964100c2200')

    if choice == "10":
        sendhex(ip, token, '000000690A2434396138643462382D306266642D346230342D393034632D6533306365656365626334641216496E76656E746F727952656D6F7465536572766963651A0F67657452656369706553746174757322181A160A145245434950455F44524F505F4F4E5F5052495A450000006D0A2433346561633530302D386431622D343435632D396564352D3362386463633863316435331216496E76656E746F727952656D6F7465536572766963651A0D6578656375746552656369706522111A0F0A0D45584348414E47455F474F4C442209120708661D000020412200000AF09F90BEF09D95B3F09D9686F09D9691F09D9691F09D9694F09D969CF09D968AF09D9693F09F8E830A')

    if choice == "55":
        banner()
        print("                >Anilibria.TV< ")
        sys.exit("       >Спасибо что выбираете нас!<")

def sendhex(ip, token, hex):
    banner()
    print(" Set method dup \n [1] 1 try dup \n [2] Spam packet in the server \n [0] Exit to menu")
    sen = input("\n >> ")
    while sen != "1" and sen != "2" and sen != "0":
        print(" Invalid input numbers")
        time.sleep(0.5)
        banner()
        print(" Set method dup \n [1] 1 try dup \n [2] Spam packet in the server \n [0] Exit to menu")
        sen = input("\n >> ")

    if sen == "0":
        menu()

    if sen == "1":
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, 2222))
        except:
            banner()
            sys.exit('\n Failed to connect to Standoff 2 server. \n Try changing the server iP!')
        x = threading.Thread(target=times, daemon=True)
        banner()
        x.start()
        sock.send(bytes.fromhex(token))
        sock.send(bytes.fromhex(hex))
        print("                Dup used")
        time.sleep(0.5)
        menu()

    if sen == "2":
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, 2222))
        except:
            banner()
            sys.exit('\n Failed to connect to Standoff 2 server. \n Try changing the server iP!')
        x = threading.Thread(target=times, daemon=True)
        banner()
        print("   Dup is started! [ CTRL + Z - Crach! ]")
        time.sleep(0.5)
        i = 0
        x.start()
        while 1:
            try:
                i += 1
                time.sleep(0.01)
                sock.send(bytes.fromhex(token))
                for _ in range(4):
                   sock.send(bytes.fromhex(hex))
                print(f' {i} - Packets |  {tt}  |  [ CTRL + Z - Crach ]\n Qiwi - 7 (902) 427 86-45 Sber - 7 (902) 427 86-45')
            except:
                sock.connect((ip, 2222))

try:
    from config import ip, token, name
except:
    banner()
    print("             >Set server to connect<")
    tt = input(" [1] Enter Token \n [2] Enter Ticket \n [0] Exit to termux\n >> ")
    if tt == "0":
        banner()
        print("                >Anilibria.TV< ")
        sys.exit("       >Спасибо что выбираете нас!<")
    if tt == "1":
        banner()
        print("             >Set server to connect<")
        token = input(" Enter token >> ")
    if tt == "2":
        banner()
        print("             >Set server to connect<")
        z = input(" Enter Ticket >> ")
        x = z.replace('  ', '')
        c = x.encode("utf-8").hex()
        token = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20" + c
    ip = input(" Enter ip (Without :2222) >> ")
    time.sleep(0.5)
    name = input(" Enter you NickName >> ")
    time.sleep(0.5)
    with open('config.py', 'w') as f:
        f.write(f'token = "{token}"\nip = "{ip}"\nname = "{name}"')
        f.close()
time.sleep(1)
from config import ip, token, name
menu()
