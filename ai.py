from module import *

for i in range(2):
    print(responses[i])

while True:
    text=input("\nwhat you want me to do  ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something is wrong retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
    
