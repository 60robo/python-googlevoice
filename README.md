# python-googlevoice
A python module for sending free SMS messages using a selenium automated browser and google voice

to use this module create a sender 
  sender = text.SMS(email, password)
 
 send as many texts as you want
  sender.send(phoneNumber, message)
  
 close the browser window
  sender.quit()
