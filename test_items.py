import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_xpath ("//form[@id='add_to_basket_form']//button[@type='submit']"))
    assert button>0, "button is not present"
  
        
     
    
