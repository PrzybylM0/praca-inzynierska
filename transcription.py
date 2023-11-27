import assemblyai
from mutagen.mp3 import MP3

def get_file_duration(file_url):
    file = MP3(file_url)
    length = round(file.info.length,2)
    return length

def get_transcription(assembly_key, file_url, language):

    assemblyai.settings.api_key = assembly_key

    transcriber = assemblyai.Transcriber()

    config = assemblyai.TranscriptionConfig(
        speaker_labels = True,  
        language_code = language,
        # speakers_expected = 2  
    )

    transcript = transcriber.transcribe(
        file_url,
        config=config    
    )

    conversation = ""
    for dialogue in transcript.utterances:
        conversation += f"Rozmówca {dialogue.speaker}: {dialogue.text}\n"

    return conversation