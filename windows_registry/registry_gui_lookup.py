import winreg
import PySimpleGUI as sg 

sg.theme('DarkTeal2')
net_name = [None]*10
ssid_ar = [None]*10
about_active = False
j = 0

#Какая ОС
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_READ) as sub_key:
        os_name = winreg.QueryValueEx(sub_key, "ProductName")
        os_name_t = os_name[0]
        #print("Операционная система: ",os_name[0])

#Версия ОС
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_READ) as sub_key:
        os_vers = winreg.QueryValueEx(sub_key, "DisplayVersion")
        os_vers_t = os_vers[0]
        #print("Версия ОС: ",os_vers[0])

#Сборка ОС
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_READ) as sub_key:
        os_build = winreg.QueryValueEx(sub_key, "BuildLab")
        os_build_t = os_build[0]
       #print("Сборка ОС: ",os_build[0])

#Пользователь SSID
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList", 0, winreg.KEY_ENUMERATE_SUB_KEYS) as sub_key:
        try:
            for i in range(10):
                user_ssid = winreg.EnumKey(sub_key,i)
                if len(user_ssid) > 15:
                    ssid_ar[j] = user_ssid
                    #print("SSID пользователей: ", ssid_ar)
                    j+=j
        except:
            lol = "lol"
        else:
            print("Не нашел SSID")

#Последний входивший пользователь
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\Microsoft\\Windows NT\\CurrentVersion\\Winlogon", 0, winreg.KEY_READ) as sub_key:
        last_user = winreg.QueryValueEx(sub_key, "LastUsedUsername")
        last_user_t = last_user[0]
        #print("Последний входивший пользователь: ",last_user[0])

winreg.CloseKey(hkey)


####################################################################

menu_def = [['File', ['Exit',]],
            ['Help', 'About...'],]

layout_main = [ [sg.Canvas(size=(500,3), background_color = "#91ff99")],
            [sg.Text('System', size = 45, font = "Helvetica 15", justification = 'c')],
            [sg.Canvas(size=(500,3), background_color = "#91ff99")],
            [sg.Menu(menu_def), sg.Text("OS Name: ", size=15,  font = "Helvetica 12"),sg.Input(os_name[0], size=50, readonly=True,  font = "Helvetica 10")],
            [sg.Text("OS Version: ", size=15,  font = "Helvetica 12"),sg.Input(os_vers[0], size=50, readonly=True,  font = "Helvetica 10")],
            [sg.Text("OS Build: ", size=15,  font = "Helvetica 12"),sg.Input(os_build[0], size=50, readonly=True,  font = "Helvetica 10")],
            [sg.Text("User SSID: ", size=15,  font = "Helvetica 12"),sg.Input(ssid_ar[0], size=50, readonly=True,  font = "Helvetica 10")], #hmmmmm
            [sg.Text("Another user SSID: ", size=15,  font = "Helvetica 12"),sg.Input(ssid_ar[1], size=50, readonly=True,  font = "Helvetica 10")],
            [sg.Text("Last entered User: ", size=15,  font = "Helvetica 12"),sg.Input(last_user[0], size=50, readonly=True,  font = "Helvetica 10")],
            [sg.Canvas(size=(500,3), background_color = "#91ff99")]]

window = sg.Window("Windows Registry View", layout_main, resizable=True, finalize=True)

while True:
    event1,values1 = window.read(timeout=100)
    if event1 == sg.WIN_CLOSED or event1 == 'Exit':
        break
    if event1 == 'About...' and not about_active:
        about_l = [[sg.Button('Back',size=(4,1),  font = "Helvetica 10")],
                   [sg.Text('   ', size = (40), justification = 'l')],
                   [sg.Text('Registry gui fast viewer', size = (40), justification = 'l', font = "Helvetica 12")],
                   [sg.Text('Created by: hakypehh', size = (40), justification = 'l', font = "Helvetica 12")],
                   [sg.Text('   ', size = (40,2), justification = 'l', font = "Helvetica 12")],
                   [sg.Text('2022', size = (40), justification = 'c', font = "Helvetica 12")]]
        about_active = True
        window.Hide()
        aboutWindow = sg.Window("About...", about_l, resizable=True,finalize=True)

        while True:
            event2,values2 = aboutWindow.read(timeout=100)
            if event2 == sg.WIN_CLOSED or event2 == 'Back':
                about_active = False
                aboutWindow.close()
                window.UnHide()
                break
        #sg.popup("Registry gui fast viewer\n"
        #        " \n"
        #        " \n"
        #         "Created by: hakypehh\n"
        #         "2022")

window.close()
