

import speech_recognition 
import wolframalpha #information source
import pyttsx3 #text to speech  
import wikipedia #another information source
import PySimpleGUI #User Interface 




def UI():
    
    
     PySimpleGUI.theme('TanBlue')
     list = [[PySimpleGUI.Text('Would you like to talk or type? ["talk"/"type"]')],
             [PySimpleGUI.Input()],
             [PySimpleGUI.Submit(), PySimpleGUI.Cancel()]]
           
     
    
    
     window = PySimpleGUI.Window('Choose communication method', list)
    
     
     event, values = window.read()
     text_input = values[0].lower()
     
     def result():
        try:
            app_id = 'G2L8HX-8LA96R6HYR'
            client = wolframalpha.Client(app_id)
            res = client.query(text_input2)
            ans = next(res.results).text
            return ans
        except StopIteration:
            wikians = wikipedia.summary(text_input2, 2)
            return wikians  
      
     window.close()
     
     if text_input == 'type':
             list2 = [[PySimpleGUI.Text('Okay, type your question in the below prompt')],
                      [PySimpleGUI.Input()],
                      [PySimpleGUI.Submit(), PySimpleGUI.Cancel()]]
             
             window2 = PySimpleGUI.Window('Assistant', list2)
             
             event2, values2 = window2.read()
             text_input2 = values2[0].lower()
             
          
             PySimpleGUI.popup('Result is:', result())
             window2.close()

     elif text_input == 'talk':
  
         r = speech_recognition.Recognizer()
         m = speech_recognition.Microphone()

         layout = [[PySimpleGUI.Text('Converter', font='Helvetica 15')],
                    [PySimpleGUI.ReadButton('Speak'), PySimpleGUI.ReadButton('Stop')],
                    #[PySimpleGUI.Output(size=(80, 10))],
                    [PySimpleGUI.Exit()]]

         window = PySimpleGUI.Window('Speech Recognition').Layout(layout)

         while True:
            event,values = window.Read()
            if event is None or event == 'Exit':
                 break
            elif event == 'Speak':
                 with m as source:
                     r.adjust_for_ambient_noise(source)
                     audio = r.listen(source)
                     audio_to_text = r.recognize_google(audio)
                     
                     
                     try:
                        
                        app_id = 'G2L8HX-8LA96R6HYR'
                        client = wolframalpha.Client(app_id)
                        res = client.query(audio_to_text)
                        ans = next(res.results).text
                        
                        PySimpleGUI.popup('Result is:', ans)  
                                        
            
                    #if wolframalpha wasn't able to provide info 2nd attempt would be wikipedia
                     except StopIteration:
                                
                        ans = wikipedia.summary(audio_to_text, 2)
                        PySimpleGUI.popup('Result is:', ans)  
                     
                     

            window.Close()
        

while True:
    
    UI()