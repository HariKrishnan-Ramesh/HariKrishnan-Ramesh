def validate_pin(pin):
        
    if len(pin) not in (4, 6):
        return False
    
    for i in pin:
        if i < '0' or i > '9':
            return False
        if (int(i)%2) == 0:
             return False
        
    return True          


pin=input("Enter Your Pin: ")
result = validate_pin(pin)
print(result)




