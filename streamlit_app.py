import streamlit
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast")
streamlit.text("🥣Yogurt, Blueberries and Granola")
streamlit.text("🐔Egg White Omelete")
streamlit.text("🥗Vegan Peanut Butter Smoothie")
streamlit.text("🥑Avocado Toast") 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana'])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)

