#streamlit FE app
import streamlit as st
from streamlit_option_menu import option_menu
def main():



    # Set page configuration
    st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")

    # Sidebar navigation menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "About", "Contact"],
            icons=["house", "info-circle", "envelope"],
            menu_icon="cast",
            default_index=0,
        )

    # Display content based on selected menu option
    if selected == "Home":
        st.title("Welcome to the Home Page")
        st.write("This is the home page of the Streamlit app.")


if __name__ == "__main__":
    main()