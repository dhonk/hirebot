import openai

def get_text(file: str, api: str):
    model_id = 'whisper-1'
    media_file_path = file
    media_file = open(media_file_path, 'rb')    

    response = openai.Audio.transcribe (
        api_key=api,
        model=model_id,
        file=media_file
        )
    
    return response['text']



