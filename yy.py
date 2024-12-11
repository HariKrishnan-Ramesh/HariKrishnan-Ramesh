def validate_pin(pin):

  if not isinstance(pin, str):
    return "Invalid"

  if len(pin) not in (4, 6):
    return False

  for digit in pin:
    if digit < '0' or digit > '9':
      return False
    if (int(digit) & 1) == 0:  
      return False

  return True

pin = input("Enter your PIN: ")
if validate_pin(pin):
  print("Valid PIN")
else:
  print("Invalid PIN")