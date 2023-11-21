import streamlit as st
import os
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# Set page layout to wide mode
st.set_page_config(layout="wide")

# Function to display images from a directory
def display_images_from_directory(directory, image_type):
    for file_name in sorted(os.listdir(directory)):
        file_path = os.path.join(directory, file_name)

        df = pd.read_csv(file_path)
        # Strip leading/trailing spaces from column names
        df.columns = df.columns.str.strip()
        
        # If HTML file, use components.html
        if file_name.endswith('.html'):
            with open(file_path, 'r', encoding="utf-8") as f:
                html_code = f.read()
                components.html(html_code, height=600)  # Set a suitable height value

         # Check if the directory is not for correlation matrices and the file is a CSV
        elif file_name.endswith('.csv'):
            

            # pour print les matrices de correlation
            if image_type == "Correlation_matrix":
                df = pd.read_csv(file_path, index_col=0)
                # Create a heatmap for the correlation matrix
                fig = px.imshow(df, 
                                x=df.columns, 
                                y=df.columns, 
                                color_continuous_scale='RdBu_r', # Red-Blue color scale, can be adjusted
                                zmin=-1, zmax=1)  # Scale for correlation ranges from -1 to 1
                fig.update_layout(xaxis_title='Features', yaxis_title='Features')
                st.plotly_chart(fig, use_container_width=True)

            # pour print les histogrammes
            elif image_type == "label" or image_type == "Labels_in_dataset":

                # Create a bar plot for histogram data
                fig = px.bar(df, x='label', y='Frequency')  # Directly use the column names
                fig.update_layout(title='Histogram Title', xaxis_title='Label', yaxis_title='Frequency')
                st.plotly_chart(fig, use_container_width=True)  # Display the figure in Streamlit


            # pour print les courbes
            else:

                # Create a line or scatter plot for other time series data
                x_col = df.columns[0]  # Typically 'Time' 
                y_col = df.columns[1]
                fig = px.line(df, x=x_col, y=y_col)  # Use px.scatter for scatter plot
                fig.update_layout(title=file_name.replace('.csv', ''), xaxis_title=x_col, yaxis_title=y_col)
                st.plotly_chart(fig, use_container_width=True) 
        
        # If PNG image, use st.image
        elif file_name.endswith('.png'):
            st.image(file_path, caption=file_name, use_column_width=True)

        

# Physical Data Exploration Page
def physical_page():
    st.subheader("Physical Data Exploration")
    root_directory = 'images/physical'
    
    dataset_exploration_directory = os.path.join(root_directory, "Dataset_exploration")
    dataset_subdirectories = [d for d in os.listdir(dataset_exploration_directory) if os.path.isdir(os.path.join(dataset_exploration_directory, d))]
    image_type = st.selectbox("Choose an exploration visualization:", [""] + dataset_subdirectories)

    if image_type:
        st.subheader(image_type)
        # Display images or data visualizations from the selected directory
        display_images_from_directory(os.path.join(dataset_exploration_directory, image_type), image_type)

    



# Network Data Exploration Page
def network_page():
    st.subheader("Network Data Exploration")
    root_directory = 'images/network'
   
    dataset_exploration_directory = os.path.join(root_directory, "Dataset_exploration")
    dataset_subdirectories = [d for d in os.listdir(dataset_exploration_directory) if os.path.isdir(os.path.join(dataset_exploration_directory, d))]
    image_type = st.selectbox("Choose an exploration visualization:", [""] + dataset_subdirectories)

    if image_type:
        st.subheader(image_type)
        # Check if the selected directory is for correlation matrices
        is_correlation_matrix = (image_type == "Correlation_matrix")
        display_images_from_directory(os.path.join(dataset_exploration_directory, image_type), image_type)

# Data Exploration Main Page
def data_exploration_page():
    st.title("Data Exploration")
    tab1, tab2 = st.tabs(["Physical", "Network"])

    with tab1:
        physical_page()

    with tab2:
        network_page()

# Results Page
def results_page():
    st.title("Results: bi-curve comparison")

    # Metrics options for the select box
    metrics_options = ["Precision", "Recall", "TPR", "TNR", "Accuracy", "F1-score", "Balanced Accuracy", "Matthews Correlation Coefficient"]
    
    # Model options for the select box
    model_options = ["KNN", "CART", "Random Forest", "XGBoost", "SVM", "MLP", "Multi-dataset"]

    # datasets
    dataset_options = ["Physical", "Network"]

    # attack categories
    attack_options = ["normal", "Dos", "Physical fault", "MITM", "scan"]

    # Create a select box for choosing a metric
    selected_metric = st.selectbox("Choose a metric to display:", metrics_options)

    # Create two columns for model selection
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Curve 1")
        # Create a select box for choosing a model in the first column
        selected_model_1 = st.selectbox("Choose a model :", model_options)
        selected_dataset_1 = st.selectbox("Choose a dataset :", dataset_options)
        selected_attack_1 = st.selectbox("Choose an attack category :", attack_options)

    with col2:
        st.subheader("Curve 2")
        # Create a select box for choosing a model in the second column
        selected_model_2 = st.selectbox("Choose a model :", model_options)
        selected_dataset_2 = st.selectbox("Choose a dataset :", dataset_options)
        selected_attack_2 = st.selectbox("Choose an attack category :", attack_options)

    # Display the selected metric and models
    # st.write(f"Selected Metric: {selected_metric}")
    # st.write(f"Selected Model in Curve 1: {selected_model_1}")
    # st.write(f"Selected Model in Curve 2: {selected_model_2}")
    
    # Placeholder for displaying the results based on the selected metric and models
    # Here you can add your code to display the results for the chosen combinations
    # For example:
    # if selected_metric == "Precision" and selected_model_1 == "KNN":
    #     # Code to display precision results for KNN in column 1
    # ... and so on for other combinations

    # Placeholder content can be replaced with actual result displaying logic
    st.write("Placeholder content for displaying results based on the selected metric and models.")


# Main function
def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("What do you want to visualize?", ("Data Exploration", "Results"))

    if choice == "Data Exploration":
        data_exploration_page()
    elif choice == "Results":
        results_page()

if __name__ == "__main__":
    main()