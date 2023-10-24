import streamlit as st
import os
import streamlit.components.v1 as components

# Set page layout to wide mode
st.set_page_config(layout="wide")

def main():
    st.title("Project Visualisation page")
    
    # Sidebar with page selection
    page_selection = st.sidebar.selectbox("Dataset type", ["Network", "Physical"])
    
    if page_selection == "Network":
        show_network()
    elif page_selection == "Physical":
        show_physical()

def show_network():
    st.header("Network Page")
    st.write("no content for now")

def show_physical():
    st.header("Physical Page")

    root_directory = 'image/physical'
    subdirectories = [d for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d))]
    
    # Ensure 'Correlation_matrix' is at the end of the list
    if 'Correlation_matrix' in subdirectories:
        subdirectories.remove('Correlation_matrix')
        subdirectories.append('Correlation_matrix')
    
    # Add a selectbox for subpages
    image_type = st.selectbox("What do you want to see?", [""] + subdirectories)

    if image_type:
        st.subheader(image_type)
        display_html_images_from_directory(os.path.join(root_directory, image_type))

def display_html_images_from_directory(directory):
    for file_name in sorted(os.listdir(directory)):
        if file_name.endswith('.html'):
            with open(os.path.join(directory, file_name), 'r') as f:
                html_code = f.read()
                components.html(html_code, height=600)  # Set a suitable height value

if __name__ == "__main__":
    main()
