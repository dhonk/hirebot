import openai

# API_KEY= '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'
#openai.api_key = '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'

def get_text(file, api):
    model_id = 'whisper-1'
    media_file_path = file
    media_file = open(media_file_path, 'rb')    

    response = openai.Audio.transcribe (
        api_key=api,
        model=model_id,
        file=media_file
        )
    
    return response['text']
    
def text():
    file_path = input("Enter the path to the MP3 file: ")

    return file_path


