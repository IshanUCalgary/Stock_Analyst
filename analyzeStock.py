import model
import view
import logging

try:
    model.yahooFinance()
except:
   logging.exception("There was an error encountered")
   model.driverQuit()
   view.fileClose()

print('Closing File...')
model.driverQuit()
view.fileClose()


    
