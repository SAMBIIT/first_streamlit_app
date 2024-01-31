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
streamlit.dataframe(my_fruit_list)
