#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

#New Section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
