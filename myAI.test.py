def test_getAIresponse(self, mock_cyClient):
    myai = myAI()  # Creating an instance of myAI class
    
    # Creating a mock response with a 'content' attribute in 'message'
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message={'content': 'Test response'})]
    
    # Setting the mock response for the chat completions create method
    mock_cyClient.chat.completions.create.return_value = mock_response  

    response = myai.getAIresponse()  # Getting the AI response

    # Asserting the response content matches the expected value
    self.assertEqual(response['content'], 'Test response')  

def test_getMyIDEAforme(self):
    myai = myAI()  # Initializing an instance of myAI class
    
    # Getting the idea from the getMyIDEAforme method
    idea = myai.getMyIDEAforme()

    # Checking if the idea matches the expected value
    self.assertEqual(idea, "formegood")