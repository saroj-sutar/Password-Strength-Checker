# Password Strength Checker

# Check if password:

# Has uppercase done
# Has numbers done
# Has special characters done
# Minimum length - 8

# Concepts used:
# Strings, loops, conditions

print("")
print("_____Password Strength Checker_____")
print("")

a = input("Enter Password : - ")
print("")

def upp (a):
    found = "no"
    for che in a:
   
        if che.isupper():
            print("✅Uppercase requirement satisfied...!")
            found = "yes"
            return True
        else:
            continue
    if  found == "no":
        print("❌Uppercase requirement not satisfied...!")
        return False
       
       
def low (a):
    found = "no"
    for che in a:
   
        if che.islower():
            print("✅Lowercass requirement satisfied...!")
            found = "yes"
            return True
        else:
            continue
    if  found == "no":
        print("❌Lowercass requirement not satisfied...!")
        return False
       

def num (a):
    f = "no"
    for ch in a:
   
        if ch.isdigit():
            print("✅Numeric requirement satisfied...!")
            f = "yes"
            return True
        else:
            continue
    if  f == "no":
        print("❌Numeric requirement not satisfied...!")
        return False
       
def sep_che (a):
    f = "no"
    for ch in a:
   
        if not ch.isalnum():
            print("✅Special_cherecter requirement satisfied...!")
            f = "yes"
            return True
        else:
            continue
    if  f == "no":
        print("❌Special_cherecter requirement not satisfied...!")
        return False
       
       
def min_che (a):
    if 8 <= len(a):
        print("✅Cherecter count > 8 requirement satisfied...!")
        return True
    else:
        print(f"❌Cherecter count > 8 requirement not satisfied : Entered {len(a)} cherecter...!")
        return False
       

if upp (a) and low (a) and num (a) and sep_che (a) and min_che (a) :
    print("")
    print("✅Password meets all the requirements...! Press Next ")
    print("")
else:
    print("")
    print("⚠️ Password does not meet all requirements. Please review the issues above and make the necessary corrections...!")
    print("")





