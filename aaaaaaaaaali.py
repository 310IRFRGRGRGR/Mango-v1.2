import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to search Google using Chrome and Selenium
def google_search():
    query = entry_query.get()
    
    if not query:
        text_box.insert(tk.END, "Please enter a search query.\n")
        return
    
    # Clear the text box
    text_box.delete(1.0, tk.END)
    
    # Set up Selenium WebDriver for Google Chrome
    driver = webdriver.Chrome(executable_path="PATH_TO_CHROMEDRIVER")
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search box, enter the query, and perform the search
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)  # Let the page load for a few seconds
    
    # Retrieve search results
    results = driver.find_elements_by_css_selector("div.g")
    
    # Display the results in the text box
    for result in results:
        title = result.find_element_by_tag_name("h3").text
        link = result.find_element_by_tag_name("a").get_attribute("href")
        text_box.insert(tk.END, f"Title: {title}\n")
        text_box.insert(tk.END, f"Link: {link}\n\n")
    
    # Close the browser
    driver.quit()

# Set up the Tkinter window
root = tk.Tk()
root.title("Google Search with Chrome")

# Search Query Entry
label_query = tk.Label(root, text="Search Query:")
label_query.pack()
entry_query = tk.Entry(root, width=50)
entry_query.pack()

# Search Button
button_search = tk.Button(root, text="Search Google", command=google_search)
button_search.pack()

# Text Box to display search results
text_box = tk.Text(root, height=20, width=80)
text_box.pack()

# Run the Tkinter event loop
root.mainloop()
