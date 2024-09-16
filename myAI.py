from openai import OpenAI

class myAI():    
    cyClient = OpenAI(base_url="https://api.chatanywhere.tech",api_key="sk-VvW6OK7ImHIIUQciLtxo88WVEj1P27rpRrkGYLG5kU7xReoP")
    MyMes = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    def setUserMes(self,oneMes):
        self.MyMes.append(oneMes)
    def getMyIDEAforme(self):
        return "formegood"
    def getUserMes(self):
        return self.MyMes
    def getAIresponse(self):
        cyCompletions = self.cyClient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= self.MyMes,
            stream=True
            
        )
        #create variables to collect the stream of events
        collected_events = []
        completion_text = ''

        #iterate through the stream of events
        for event in cyCompletions:   
            collected_events.append(event)  # save the event response
            event_text = event.choices[0].delta.content  # Extract the text

            if event_text:
                completion_text += event_text  # append the text
                print(event_text,end="")
        
        print('\n')
        #print(completion_text)
        #return cyCompletions.choices[0].message 
        