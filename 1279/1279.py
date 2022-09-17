def is_bissexual(year):

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):

        return True
        
    else:
        
        return False

def has_event_huluculu(year):

    if (year % 15 == 0):
        
        return True
    
    else:

        return False

def has_event_bulukulu(year):

    if (is_bissexual(year) == True and year % 55 == 0):

        return True

    else:

        return False


while True:

    try:
        year = int(input())
       
        if(is_bissexual(year)):

            print("This is leap year.")
            
        if(has_event_bulukulu(year)):

            print("This is bulukulu festival year.")

        if(has_event_huluculu(year)):

            print("This is huluculu festival year.")

        if((is_bissexual(year) == False) and (has_event_bulukulu(year) == False) and (has_event_huluculu(year) == False)):

                print("This is an ordinary year.")

    except EOFError:
        break