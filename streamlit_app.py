import streamlit
import pandas 
import requests 
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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
#New Section to diplay fruityvice api reponse
streamlit.header('Fruityvice is N-I-C-E') 
fruit.choice = streamlit.text_input('What fruit?,'Kiwi')
streamlit.write('The user entered ', fruit_choice)                       
#fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
