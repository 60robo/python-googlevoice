# python-googlevoice
A python module for sending free SMS messages using a selenium automated browser and google voice

to use this module create a sender 
  sender = text.SMS(email, password)
 
 send as many texts as you want
  sender.send(phoneNumber, message)
  
 close the browser window
  sender.quit()


# known Limitations
1. the program does not work when run the browser is run in headless mode
2. the browser fails to get the right pages about 20 percent of the time
