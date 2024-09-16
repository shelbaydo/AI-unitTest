import myAI
cyai = myAI.myAI()
while True:
    print("hi,this is chatGPT ,how can I help you enter 'N' to close this window\n")
    user_input = input("you: ")
    if user_input=='N':
        break
    else:
        uMes = {"role": "user", "content": f"{user_input}"}
        cyai.setUserMes(uMes)
        cyai.getAIresponse()
        
print("welcome next time")