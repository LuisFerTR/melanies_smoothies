# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("My Parents New Healthy Diner")
st.subheader("Breakfast Menu")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

# name_on_order = st.text_input('Name on Smoothie')
# st.write('The name on your Smoothie will be:', name_on_order)

# cnx = st.connection("snowflake")
# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)


