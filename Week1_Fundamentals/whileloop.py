password = 'myPassword123'
max_attempt = 3
attempt = 0
while attempt < max_attempt:
  attempt_pwd = input("Enter password: ")
  if password == attempt_pwd:
    print("Access Granted!")
    break
  else:
    print("Incorrect password. Try again")
    attempt += 1
