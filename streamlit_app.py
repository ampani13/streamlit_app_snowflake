import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# new section
streamlit.header('Fruityvice Fruit Advice!')

try:
    fruit_choice = streamlit.text_input('what fruit info you want?')
    if not fruit_choice:
        streamlit.error("please select a fruit to get info");
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()


streamlit.header('fruit load list contains:')
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
        return my_cur.fetchall()
    
    
    
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
    

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO fruit_load_list VALUES ('"+"jackfruit, papaya, guava, kiwi"+"')")
        return 'Thanks for adding '+ new_fruit
 
add_my_fruit = streamlit.text_input('what fruit would you like to add?')
if streamlit.button('add fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.write(back_from_function)
    
    
    
streamlit.stop()
    
fruit_choice = streamlit.text_input('what fruit info you want?', 'kiwi')
streamlit.write('user entered ', fruit_choice)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)


my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)


add_my_fruit = streamlit.text_input('what fruit would you like to add?', 'Kiwi')
streamlit.write('Thanks for adding ', add_my_fruit)


my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit')")
