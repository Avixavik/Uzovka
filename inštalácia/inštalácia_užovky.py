from colorama import Fore, Back, Style
import os
import sys
import time
import zipfile
import winreg as reg

def cls():
    # Pre Windows 'cls', pre Linux/Mac 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def register_extension(ext, file_type, app_path, description, icon_path):
    with reg.CreateKey(reg.HKEY_CLASSES_ROOT, ext) as key:
        reg.SetValue(key, "", reg.REG_SZ, file_type)

    with reg.CreateKey(reg.HKEY_CLASSES_ROOT, file_type) as key:
        reg.SetValue(key, "", reg.REG_SZ, description)

    with reg.CreateKey(reg.HKEY_CLASSES_ROOT, rf"{file_type}\DefaultIcon") as key:
        reg.SetValue(key, "", reg.REG_SZ, icon_path)

    shell_command = rf'"{app_path}" "%1"'
    with reg.CreateKey(reg.HKEY_CLASSES_ROOT, rf"{file_type}\shell\open\command") as key:
        reg.SetValue(key, "", reg.REG_SZ, shell_command)



def main():
    global pth 
    pth = r"C:\Program Files\Užovka"
    cls()

    print("""\033[33m
             \033[33m=========== 
            \033[33m=========  ==
            \033[33m=============
  \033[33m=================\033[93m++++             \033[96mVytajte v inštalácii užovky!
\033[33m===================\033[93m++++++
\033[33m==================\033[93m ++++++
\033[33m=========\033[93m       +++++++++
\033[33m======\033[93m ++++++++++++++++++
\033[33m======\033[93m+++++++++++++++++++
  \033[33m====\033[93m+++++++++++++++++              \033[34m[Enter] - Inštalovať
\033[93m+++++++++++++                        \033[34m[  U  ] - Ukončiť
\033[93m++  +++++++++            
\033[93m +++++++++++    
""")

    if input("\033[34m").lower() == 'u':
        cls()
        print("\033[0mInštalácia zrušená.")
        time.sleep(1)
        sys.exit(0)

    cls()
    print("""\033[33m
             \033[33m=========== 
            \033[33m=========  ==
            \033[33m=============
  \033[33m=================\033[93m++++             \033[96mInštaluje sa užovka...
\033[33m===================\033[93m++++++
\033[33m==================\033[93m ++++++
\033[33m=========\033[93m       +++++++++
\033[33m======\033[93m ++++++++++++++++++
\033[33m======\033[93m+++++++++++++++++++
  \033[33m====\033[93m+++++++++++++++++
\033[93m+++++++++++++
\033[93m++  +++++++++            
\033[93m +++++++++++    
""")

    zip_file = "užovka.zip"
    print(f"\033[0mExtrahuje sa {zip_file} do {pth}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Extrahovat do priecinku ulozeneho v pth
        zip_ref.extractall(pth)
        print("\033[32mSúbory boli úspešne extrahované.")
    
    input("\033[34m[Enter] - Pokračovať...")
    

    ext = ".už"
    file_type = "Uzovka.File"
    app_path = r"C:\Program Files\Užovka\užovka.exe"
    description = "Súbor Užovky"
    icon_path = r"C:\Program Files\Užovka\už.ico"

    try:
      print(f"\033[0mRegistruje sa prípona {ext}...")
      register_extension(ext, file_type, app_path, description, icon_path)
      print("\033[32mPrípona .už bola úspešne zaregistrovaná.")
    except PermissionError:
      cls()
      print("\033[31mChýbajúce oprávnenia.\033[0m")
      time.sleep(1)
      sys.exit(1)

    time.sleep(1)
    cls()
    print("""\033[33m
             \033[33m=========== 
            \033[33m=========  ==
            \033[33m=============
  \033[33m=================\033[93m++++             \033[32mHotovo!
\033[33m===================\033[93m++++++
\033[33m==================\033[93m ++++++
\033[33m=========\033[93m       +++++++++
\033[33m======\033[93m ++++++++++++++++++
\033[33m======\033[93m+++++++++++++++++++
  \033[33m====\033[93m+++++++++++++++++              \033[34m[Enter] - Ukončiť
\033[93m+++++++++++++
\033[93m++  +++++++++            
\033[93m +++++++++++    
\033[0m""")
    
    input()
    sys.exit(0)




main()