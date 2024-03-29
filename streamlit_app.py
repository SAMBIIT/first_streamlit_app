import streamlit

streamlit.title ('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('1. 🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('2. 🥗  Kale, Spinach & Rocket Smoothie')
streamlit.text('3. 🐔 🍞 Hard-Boiled Free-Range Egg')
streamlit.text('4. 🥑 Vitamin ABC Smothiee')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice= streamlit.text_input('What fruit would you like information about?', 'Kiwi') #kiwi here is default value, we can change and put our own input
streamlit.write('The user entered',fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())  #this just writes data to the screen

# taking the json version of the response and normalizing it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)
