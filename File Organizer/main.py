from organizer import File_Organizer

print(dir(File_Organizer))

menu = """
=================================
      Smart File Organizer
=================================

1. Select Folder
2. Show Files
3. Organize Files
4. Statistics
5. Exit
"""

if __name__ == '__main__':
    
    organizer = File_Organizer()
    while True:
        print(menu)
        try: 
            user_input = int(input("Enter your choice. : "))
        except ValueError:
            print("Enter a valid input.")
            continue
        else:
            match user_input:
                case 1:
                    success, message = organizer.select_folder()
                    print(message)
                case 2:
                    success, message = organizer.show_files()
                    print(message)
                case 3:
                    success, message = organizer.organize_files()
                    print(message)
                case 4:
                    success, message = organizer.get_statistics()
                    print(message)
                case 5:
                    print("GoodByee")
                    break
                case _:
                    print("Invalid Choice.")