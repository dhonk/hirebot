import streamlit as st
import os
import json
import grader
import time

# Set Streamlit settings
st.set_page_config(page_title="Litty", page_icon="🗣️", layout="wide", initial_sidebar_state="auto")

# Set API in grader
grader.set_api()

# Let user select the mp3 files
uploaded_files = st.file_uploader('Select the mp3 files:', type=['mp3'], accept_multiple_files=True)

# Let user input the output file name
output_file = st.text_input('Enter the name for the output JSON file:')

# Let user select the prompt file
prompt_file = st.file_uploader('Select the prompt file:', type=['txt'])

if st.button('Check file'):
    if os.path.exists(output_file):
        confirm = st.checkbox("Output file already exists. Do you want to overwrite it?")
        if not confirm:
            output_file = ''

# Perform analysis and write to the JSON file
analysis_complete = False # Flag to check analysis completion 
if st.button('Start Analysis'):
    if uploaded_files and output_file and prompt_file:
        progress_bar = st.progress(0)
        for i, file in enumerate(uploaded_files):
            # Write the uploaded file to a temporary file first so grader can read it
            temp_file_path = os.path.join(os.getcwd(), file.name)
            with open(temp_file_path, 'wb') as f:
                f.write(file.getvalue())

            grader.result(temp_file_path, prompt_file.name)
            os.remove(temp_file_path)  # Remove temporary file

            progress_bar.progress((i + 1) / len(uploaded_files))
            time.sleep(0.1)  # Adding a small delay to see the progress visually
        st.success('Analysis done!')
        analysis_complete = True

# Display the output JSON file
if analysis_complete:
    if st.button('Show JSON'):  
        with open(output_file, 'r') as f:
            data = json.load(f)
            for key in data.keys():
                st.write(f'Key: {key}')
                nested_data = data[key]
                for nested_key in nested_data.keys():
                    score = nested_data[nested_key]['Score']
                    st.write(f'{nested_key}: {score}')
                
                if st.button(f'Show more details for {key}'):
                    st.json(nested_data)
else:
        st.write("JSON file is not yet available. Please run the analysis first.")

