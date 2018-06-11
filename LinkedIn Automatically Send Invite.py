
# coding: utf-8

# In[9]:


from selenium import webdriver


# In[1]:


# Change the information in the below dictionary
Info = {
    # Your account info
    'username': 'XXX',
    'password': 'XXX',
    
    # the homepage link of the person you want to add 
    'target_link': 'https://www.linkedin.com/in/XXX',
}

# The invitation text you want to send, No more than 300 words
invite_text = "XXX"


# In[2]:


def LinkedIn_Add_Connect(Info, invite_text):
    """
    func: automatically add people and send invitation text
    """
    # the path of chromedriver
    chromedriver = path
    # Open LinkedIn 
    url = 'https://www.linkedin.com'
    browser = webdriver.Chrome(chromedriver)
    browser.get(url)
    # Sing in LinkedIn
    username_field = browser.find_element_by_id('login-email')
    password_field = browser.find_element_by_id("login-password")
    
    username = Info.get('username')
    password = Info.get('password')
    username_field.send_keys(username)
    browser.implicitly_wait(1)
    password_field.send_keys(password)
    browser.implicitly_wait(1)
    # Click for sign in 
    browser.find_element_by_id('login-submit').click()
    # Check tab title
    print("Tag title: " + browser.title)

    # Open new page
    browser.execute_script("window.open('{}', 'new_window')".format(Info.get('target_link')))
    # Switch to the new page
    # https://stackoverflow.com/questions/37088589/selenium-wont-open-a-new-url-in-a-new-tab-python-chrome
    browser.switch_to.window(browser.window_handles[1])
    # Check title
    print("Tag title: " + browser.title)
    
    # Click Connect
    browser.find_element_by_class_name('pv-s-profile-actions').click()
    
    # Click add note
    browser.find_element_by_class_name('send-invite__actions').click()
    
    invite_field = browser.find_element_by_id('custom-message')
    # Write message
    invite_field.send_keys(invite_text)
    # Click send message button
    browser.find_element_by_css_selector('.button-primary-large.ml1').click()
    # Quick 
    browser.quit()
    print('Success!')


# In[ ]:


if __name__ == "__main__":
    LinkedIn_Add_Connect(Info, invite_text)

