choice = ""
while choice != '4':
  print("\n=== Menu ===")
  print("1. Start game")
  print("2. Settings")
  print("3. Help")
  print("4. Quit")

  choice = input("Choose option: ")

  if choice == "1":
    print("Starting game...")
  elif choice == "2":
    print("Opening settings...")
  elif choice == "3":
    print("Showing help...")
  elif choice == '4':
    print("Good bye!!")
  else:
    print("invalid choice !!")
