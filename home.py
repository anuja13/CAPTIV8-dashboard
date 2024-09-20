import streamlit as st
import pandas as pd
import os

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
</style>
"""
# page_config
st.set_page_config(
    page_title='Captiv8 Dataset',
    layout="centered",
    initial_sidebar_state="expanded"
    
)

def home_page():
    # Define the path to the folder containing the Excel files
    diag_path = 'data/diag_data'
    img_text_folder = 'data/img_text_pair'

   

    st.title('CAPTIV8 - A comprehensive large scale CAPsule endoscopy dataset for Integrated diagnosis')

    st.markdown("<h4>Introduction</h4> The dataset contains images and videos of wireless capsule endoscopic examinations of patients conducted using the PillCAM colon 2 capsule. In addition, it includes alphanumeric metadata comprising of diagnostic summaries from colonoscopy and histopathology reports.", unsafe_allow_html=True)
    st.markdown("The data comprises of: <ul><li> Video, image as well as text data from 3 different diagnostic modalities, colonoscopy, histopathology and capsule endoscopy.</li><li> Six anatomical landmarks that provide crucial information to localize abnormalities with respect to the colon.</li><li> Data for radiometric and geometric caliberation of Pillcameras.</li> </ul>",unsafe_allow_html=True)

    st.markdown("The data can be visualized interactively here.")

    # Write and add image of 3D camera caliberation


    # Create a selector for the user to choose a patient number (1 to 10)
    #selected_patient = st.selectbox('Display dianostic data for ID:', list(range(1, 11)))

    st.markdown("""
        <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border-radius: 12px;
            font-size: 16px;
            margin: 5px;
        }
        </style>
        """, unsafe_allow_html=True)
    # Create a 2-row, 5-column layout for patient buttons (1 to 10)
    st.write("### Select a Patient by Pressing the Button Below:")
    cols = st.columns(5)  # Create 5 columns per row

    # Track which button is pressed
    selected_patient = None

    # First row (Patient 1 to 5)
    for i in range(1, 6):
        if cols[i - 1].button(f"P{i}", key=f'btn_{i}'):
            selected_patient = i

    # Second row (Patient 6 to 10)
    cols = st.columns(5)
    for i in range(6, 11):
        if cols[i - 6].button(f"P{i}", key=f'btn_{i}'):
            selected_patient = i

    # If a patient button is pressed, display their diagnostic data
    if selected_patient:

        # Construct the file name based on the selected patient number
        file_name = f'P{selected_patient:03}.csv'
        file_path = os.path.join(diag_path, file_name)
        # Read the selected patient's Excel file into a DataFrame
        df = pd.read_csv(file_path, index_col=False)

        # Add a column for the patient number
        df['Patient Number'] = selected_patient

        # Display the DataFrame for the selected patient in Streamlit
        st.write(f"Diagnostic Data for selected ID {selected_patient}")
        st.dataframe(df.iloc[:, :-1])
        
        # Create a button to show random images and diagnostic captions
        # Add custom CSS to style the button
        # Construct the path to the corresponding CSV file in img_text_pair folder
        img_text_file = os.path.join(img_text_folder, f'P{selected_patient:03}.csv')

        # Read the CSV file into a DataFrame
        img_df = pd.read_csv(img_text_file)

        # Select 4 random rows from the DataFrame
        random_rows = img_df.sample(n=4)

        # Display the images and their corresponding captions
        st.write(f"#### Images and Diagnostic Captions for Patient {selected_patient}")
        # Use custom CSS to increase the font size of captions
        st.markdown("""
        <style>
        .caption {
            font-size: 20px; /* Increase caption font size */
            margin-bottom: 10px; /* Space between images and captions */
        }
        </style>
        """, unsafe_allow_html=True)

        # Display images in a 2x2 grid
        cols = st.columns(2)
        for i, (index, row) in enumerate(random_rows.iterrows()):
            with cols[i % 2]:
                st.image(row['image_path'], width=200)
                st.markdown(f"<div class='caption'>{row['image_label']}</div>", unsafe_allow_html=True)


st.set_option("client.showErrorDetails", "false")
pg = st.navigation([
    st.Page(home_page, title="HOME"),
    st.Page("calibration_page.py", title="CAMERA CALIBRATION"),
])
pg.run()





