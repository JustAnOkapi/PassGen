from browser import ajax
from browser import document as doc
from browser import window
from browser import alert
from browser.widgets.dialog import InfoDialog
# imports from Brython

window.console.clear() # clean browser console 

global_key = -9 # define global key

def encode(inp, key): # derfine encode
    return "".join(map(lambda x: chr(ord(x) + key), inp)) # convert to and from ASCII adding or subtracting a value

def show(ev): # display dialog 
    inp_user = doc['input_user'].value # grab value from browser
    inp_site = doc['input_site'].value # grab value from browser
    inp_pass = doc['input_pass'].value # grab value from browser
    print(f"inp_user: {inp_user}") # console log
    print(f"inp_site: {inp_site}") # console log
    print(f"inp_pass: {inp_pass}") # console log
    
    if inp_pass == "" or inp_site == "" or inp_pass == "":
        doc['bodyy'] <= "Please fill out inputs!\n" # error for empty space
        raise SystemExit 
    
    
    if len(inp_site) < 6: # if site name is too small
        inp_site = inp_site + inp_site + inp_site # triple its size 
    
    site_key1 = ord(inp_site[:1]) # ord of first letter
    site_key2 = ord(inp_site[1:2]) # ord of second letter
    site_key3 = 0 # starting value
    for letter in inp_site[3:]:
        site_key3 += ord(letter) # ord of rest of letters

    
    moving_pass = inp_pass # make temp moving pass
    
    moving_pass = encode(moving_pass, site_key1) # first encode
    moving_pass = encode(moving_pass, site_key2) # second encode
    moving_pass = encode(moving_pass, site_key3) # third encode
    
    
    end_pass = moving_pass + encode(inp_user, global_key) # duplicate with offset
    
    InfoDialog("New Password: ", f"{end_pass}") # display the new pass

def run(): # bind button clicked to show
    doc["run_button"].bind("click", show)

if __name__ == 'mainPY': # when file accesed
    run() # run run
    
