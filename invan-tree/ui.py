print("""
 _____ _   _ _   _  ___   _   _      ___________ _____ _____ 
|_   _| \ | | | | |/ _ \ | \ | |    |_   _| ___ \  ___|  ___|
  | | |  \| | | | / /_\ \|  \| |______| | | |_/ / |__ | |__  
  | | | . ` | | | |  _  || . ` |______| | |    /|  __||  __| 
 _| |_| |\  \ \_/ / | | || |\  |      | | | |\ \| |___| |___ 
 \___/\_| \_/\___/\_| |_/\_| \_/      \_/ \_| \_\____/\____/ """)
print("\n")
print("  Alpha Version 0.0.1")
print("  MIT Licence")
print("  Made by Ethan \u00a9 2021")
print("-------------------------------------------------------------")

print("\n")
waiting_for_input = True
while waiting_for_input:
    print("""Please select:
--------------""")
    print("1: Search for item, 2: Search By Stock Number, 3: Delete Items")
    print("------------------------------------------------------------------------------------------------------")
    question = input("")

    if question == "1":

        print("Input Item Name:")
        see_item = input()
        if see_item == "ASICS":
            print("\n")
            print("Brand " + "\tModel" + "\t\tStock Number" + "\tQuantity" + "\tPrice")
            print("-----" + "\t-----" + "\t\t------------" + "\t--------" + "\t-----")
            print(f"ASICS\t GT-1000 10\t 52541903 \t5 \t\t£45.00")
            print(f"ASICS\t GEL-CONTEND 6\t 52544202 \t3 \t\t£40.00")
            print("\n")
    elif question == "2":
        print("Input Stock Number:")
        new_item = input()
        print("\n")
        print("Brand " + "\tModel" + "\t\tStock Number" + "\tQuantity" + "\tPrice")
        print("-----" + "\t-----" + "\t\t------------" + "\t--------" + "\t-----")
        print(f"ASICS\t GT-1000 10\t 52541903 \t5 \t\t£45.00")
        print("\n")
    elif question == "3":
        print("Enter Key Of Item To Delete:")
        input()

    elif question == "exit" or "quit":
        print("Thank You For Using Invan-Tree!")
        waiting_for_input = False
    else:
        print("")


