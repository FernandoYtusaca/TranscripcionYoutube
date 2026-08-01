from youtube_transcript_api import YouTubeTranscriptApi

video_id = "KQFPzJX4CsE"

try:
    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["es", "en"])

    start_time = 200      # 03:20
    end_time = 490       # 08:10

    texto = []

    for entry in transcript:
        if start_time <= entry.start <= end_time:
            texto.append(entry.text)

    with open("transcripcion.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(texto))

    print("Transcripción guardada en transcripcion.txt")

except Exception as e:
    print("Ocurrió un error:")
    print(e)