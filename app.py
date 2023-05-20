import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to get frequencies of words on a webpage
def get_word_frequency(url):
    # Send a GET request to the url
    response = requests.get(url)

    # Parse the response
    soup = BeautifulSoup(response.text,'html.parser')
    # Extracting the text from html
    soup_text = soup.get_text()

    # Spliting text into separate words
    words_list = soup_text.split()

    word_frequency = {}

    for word in words_list:
        if word_frequency.get(word):
            # Increment frequency by 1 if the word already exists
            word_frequency[word] += 1 
        else:
            # If word is not in frequency dictionary then set value 1
            word_frequency[word] = 1 
    
    # Return the frequency of the words
    return word_frequency

def get_webpage_text():
    # Title of the application
    st.title("Word Frequency Analyzer")
    # Get url input from user
    url = st.text_input("Enter the url of the web page you want to analyze")

    # Check if button is clicked
    if st.button("Analyze"):
        # If url is provided
        if url:
            # getting frequency of words
            word_frequency = get_word_frequency(url)
            st.write("Frequency of word occurrence: ")
            # Show output as Json object
            st.json(word_frequency)
        
        # If no url is provided
        else:
            st.warning("Please enter the url of the web page")


if __name__ == '__main__':
    get_webpage_text()