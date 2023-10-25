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
    root_directory = 'images/network'

    # Add a sidebar selection for Dataset Exploration or Results
    network_page_selection = st.sidebar.selectbox("Choose a section:", ["Dataset Exploration", "Results"])

    # Depending on the selection, display the appropriate selectbox and content
    if network_page_selection == "Dataset Exploration":
        dataset_exploration_directory = os.path.join(root_directory, "Dataset_exploration")
        dataset_subdirectories = [d for d in os.listdir(dataset_exploration_directory) if os.path.isdir(os.path.join(dataset_exploration_directory, d))]
        image_type_dataset = st.selectbox("Choose an exploration visualization:", [""] + dataset_subdirectories)

        if image_type_dataset:
            st.subheader(image_type_dataset)
            display_images_from_directory(os.path.join(dataset_exploration_directory, image_type_dataset))
            
    elif network_page_selection == "Results":
        results_directory = os.path.join(root_directory, "Results")
        results_subdirectories = [d for d in os.listdir(results_directory) if os.path.isdir(os.path.join(results_directory, d))]
        image_type_results = st.selectbox("Choose a model:", [""] + results_subdirectories)

        if image_type_results == "KNN":
            st.subheader(image_type_results)
            # Display images from KNN/Confusion_matrix directory
            display_images_from_directory(os.path.join(results_directory, image_type_results, "Confusion_matrix"))
        elif image_type_results == "Random_forest":
            st.subheader(image_type_results)
            # Display images from Random_forest/Confusion_matrix directory
            display_images_from_directory(os.path.join(results_directory, image_type_results, "Confusion_matrix"))
        elif image_type_results:
            st.subheader(image_type_results)
            display_images_from_directory(os.path.join(results_directory, image_type_results))


def show_physical():
    st.header("Physical Page")
    root_directory = 'images/physical'

    # Add a sidebar selection for Dataset Exploration or Results
    physical_page_selection = st.sidebar.selectbox("Choose a section:", ["Dataset Exploration", "Results"])

    # Depending on the selection, display the appropriate selectbox and content
    if physical_page_selection == "Dataset Exploration":
        dataset_exploration_directory = os.path.join(root_directory, "Dataset_exploration")
        dataset_subdirectories = [d for d in os.listdir(dataset_exploration_directory) if os.path.isdir(os.path.join(dataset_exploration_directory, d))]
        image_type_dataset = st.selectbox("Choose an exploration visualization:", [""] + dataset_subdirectories)

        if image_type_dataset:
            st.subheader(image_type_dataset)
            display_images_from_directory(os.path.join(dataset_exploration_directory, image_type_dataset))
            

    elif physical_page_selection == "Results":
            results_directory = os.path.join(root_directory, "Results")
            results_subdirectories = [d for d in os.listdir(results_directory) if os.path.isdir(os.path.join(results_directory, d))]
            image_type_results = st.selectbox("Choose a model:", [""] + results_subdirectories)

            if image_type_results == "KNN":
                st.subheader(image_type_results)
                # Display images from KNN/Confusion_matrix directory
                display_images_from_directory(os.path.join(results_directory, image_type_results, "Confusion_matrix"))
            elif image_type_results == "Random_forest":
                st.subheader(image_type_results)
                # Display images from Random_forest/Confusion_matrix directory
                display_images_from_directory(os.path.join(results_directory, image_type_results, "Confusion_matrix"))
            elif image_type_results:
                st.subheader(image_type_results)
                display_images_from_directory(os.path.join(results_directory, image_type_results))




def show_results():
    st.subheader("Results Page")
    st.write("This is the content of the Results page.")
    # Add your code to display content for the Results page here

def display_images_from_directory(directory):
    for file_name in sorted(os.listdir(directory)):
        file_path = os.path.join(directory, file_name)
        
        # If HTML file, use components.html
        if file_name.endswith('.html'):
            with open(file_path, 'r',encoding="utf-8") as f:
                html_code = f.read()
                components.html(html_code, height=600)  # Set a suitable height value
        
        # If PNG image, use st.image
        elif file_name.endswith('.png'):
            st.image(file_path, caption=file_name, use_column_width=True)

if __name__ == "__main__":
    main()
