import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

#import streamlit
#streamlit.title('My Parents New Healthy Diner')
#streamlit.header('Breakfast Menu')
#streamlit.text('Omega 3 & Blueberry Oatmeal')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg')


# import streamlit 
streamlit.header(' My Parents New Healthy Diner') 
streamlit.title('Breakfast Menu') 
streamlit.text ('🥣Omega-3 and blueberry oatmeal') 
streamlit.text('🥬Kale,Spinach & Rocket smoothie') 
streamlit.text('🐔Hard-boiled free range eggs') 
streamlit.text('🥑🍞Avocado Toast') 
streamlit.header('🍌🍐Build your own fruit smoothie🍑🥝') 

# import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit') 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected] 
streamlit.dataframe(fruits_to_show) 

# ***** BEFORE CODE *******
# New Section to display fruityvice api response 
# streamlit.header("Fruityvice Fruit Advice!") 
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) 

# import pandas
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
# streamlit.dataframe(fruityvice_normalized)
# ******  BEFORE CODE ABOVE ************

# create the repeatable code block (called a function) 
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

# New Section to display fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!") 
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
   else:
      back_from_function = get_fruityvice_data(fruit_choice)
      stream.dataframe(back_from_function)
      
      #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      #fruityvice_normalized = pandas.json_normalized(fruityvice_response.json())
      #stream.dataframe(fruityvice_normalized) 
      
except URLError as e:
  streamlit.error() 
  
streamlit.write('The user entered ', fruit_choice)

# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) 



# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
# streamlit.dataframe(fruityvice_normalized)


# write your own comment -what does the next line do? 
# fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalize)

#import requests fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon") 
#streamlit.text(fruityvice_response)

# don't run anything past here while we troubeshoot
streamlit.stop()

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text("The fruit load list contains:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
# add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)

# This will not wprk correctly, but just go with it for now
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
      with my_cnx.cursor() as my_cur:
            my_cur.execute('insert into fruit_load_list values ('lemon')")
            return "Thanks for adding " + new_fruit
                           
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamli.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)
                           

