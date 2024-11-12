import yt_dlp
from youtubesearchpython import VideosSearch

# Lista de músicas que você quer baixar
musicas = [
    "Eduardo Costa - Vê se volta comigo",
    "Zezé de Camargo e Luciano - Será que foi saudade",
    "Bruno e Marrone - Não tem outro jeito",
    "Maida e Marcelo - porque brigamos",
    "Renan e Ray - Coração ferido"
]

def baixar_musica(video_url, novo_nome):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{novo_nome}.%(ext)s',  # Nome do arquivo de saída
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

for index, musica in enumerate(musicas):
    # Buscar o vídeo no YouTube pelo nome da música
    search = VideosSearch(musica, limit=1)
    result = search.result()
    
    # Pegar a URL do primeiro resultado
    video_url = result['result'][0]['link']
    print(f"Baixando {musica} de {video_url}...")

    # Formatar o novo nome de arquivo
    novo_nome = f"{index + 1}. {musica}"
    
    # Baixar o vídeo como MP3 com o novo nome
    baixar_musica(video_url, novo_nome)

print("Download completo!")
