import time
from dotenv import load_dotenv
import os
from gmail_api import send_email
from transcription import get_transcription, get_file_duration
from chat_gpt import  get_chatgpt_response
from config import LANGUAGE, SCOPES, SUBJECT, CHATGPT_MODEL


def operation(num, file_path, to):
    load_dotenv()
    ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    start_time = time.time()
    print("\n\n\nGeneruję krótkie streszczenie...")
    transcription_result = get_transcription(ASSEMBLYAI_API_KEY, file_path, LANGUAGE)
    print("Proces transkrypcji zakończony pomyślnie (1/4)")
    file_duration = get_file_duration(file_path)
    with open("./raw_transcription_files/transcription_result.txt", "w", encoding="utf-8") as file:
        file.write(transcription_result)
    print("Treść transkrypcji zapisano do pliku: [transcription_result.txt] (2/4)")
    response = get_chatgpt_response(num, OPENAI_API_KEY, transcription_result, CHATGPT_MODEL)
    print("Proces analizy treści zakończony pomyślnie (3/4)")
    send_email(SUBJECT, response, to, "./raw_transcription_files/transcription_result.txt", SCOPES)
    print("Wynik analizy rozmowy:")
    print(response)
    end_time = time.time()
    time_result = round(end_time - start_time, 2)
    print(f"Proces przetwarzania danych trwał: {time_result} sekund")
    print(f"Czas trwania przetwarzanego pliku audio: {file_duration} sekund")

def main():
    global file_path
    file_path=""
    global to
    to=""
    while True:
        print("==================================================|")
        print("Rozpocznij proces analizy rozmowy od kroku nr.1")
        print("[1] Wskaż ścieżkę do pliku z audio")
        print("[2] Wskaż docelowy adres e-mail\n")

        print("[3] Wygeneruj krótkie streszczenie [do 80 słów]")
        print("[4] Wygeneruj długie streszczenie [do 300 słów]")
        print("[5] Wygeneruj słowa kluczowe")
        print("[6] Wygeneruj analize sentymentu")
        print("[7] Wygeneruj spis treści\n")

        print("[8] Wyjście")
        print("==================================================|")

        num = input("Wybierz opcję: ")

        operations = {
            '3': operation,
            '4': operation,
            '5': operation,
            '6': operation,
            '7': operation,
        }

       

        if num == '1':
            file_path = input("Podaj ścieżkę do pliku audio (mp3): ")
            print(f'Ścieżka do pliku: {file_path}')
            print("Przejdź do kroku nr.2\n\n")

        elif num == '2':
            to = input("Podaj adres e-mail, na który wysłać analizę rozmowy: ")
            print(f'Podany adres e-mail: {to}')
            print("Przejdź do wyboru rodzaju analizy rozmowy w krokach nr.3-7\n\n")

        elif num in operations:
            if not file_path:
                print("Nie podano ścieżki do pliku audio (spróbuj ponownie)")
            elif not to:
                print("Nie podano adresu docelowego e-mail (spróbuj ponownie)")
            else:
                operation(num, file_path, to)
            
        elif num == '8':
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
