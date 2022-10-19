import streamlit

import pandas 

fruits_selected = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.title("My parents new healty diner")

streamlit.header("Breakfast menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

