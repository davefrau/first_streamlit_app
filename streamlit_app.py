import streamlit
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast")
streamlit.text("🥣Yogurt, Blueberries and Granola")
streamlit.text("🐔Egg White Omelete")
streamlit.text("🥗Vegan Peanut Butter Smoothie")
streamlit.text("🥑Avocado Toast") 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)

