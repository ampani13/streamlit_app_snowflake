import streamlit
import pandas
import snowflake.connector

streamlit.title('Amiya is best ek no')

streamlit.header('Amiya\'s Pros:')
streamlit.text('smart')
streamlit.text('intelligent')
streamlit.text('helpful')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


# new section
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('what fruit info you want?', 'kiwi')
streamlit.write('user entered ', fruit_choice)

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)


my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)


streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)
