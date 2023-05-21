import streamlit as st
import os
import grader
import time

def _analysis(files, prompt_file):
    if files and prompt_file:
        with st.form("analysis"):
            progress_bar = st.progress(0)
            for i, file in enumerate(files):
                # Write the uploaded file to a temporary file first so grader can read it
                temp_file_path = os.path.join(os.getcwd(), file.name)
                print(f'Path: {temp_file_path}')
                with open(temp_file_path, 'wb') as f:
                    f.write(file.getvalue())

                # Assuming the second argument is the prompt file's name
                grader.result(temp_file_path, prompt_file.name)
                os.remove(temp_file_path)  # Remove temporary file

                progress_bar.progress((i + 1) / len(files))
                time.sleep(0.1)  # Adding a small delay to see the progress visually
            if st.form_submit_button("Start Analysis"):
                st.success('Analysis done!')

def app():
    # Let user select the mp3 files
    uploaded_files = st.file_uploader('Select the mp3 files:', type=['mp3'], accept_multiple_files=True)

    # Let user select the prompt file
    prompt_file = st.file_uploader('Select the prompt file:', type=['txt'])
    
    _analysis(uploaded_files, prompt_file)

if __name__ == "__main__":
    app()
