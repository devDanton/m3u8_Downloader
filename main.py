import os
import yt_dlp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PASTA_M3U8 = os.path.join(BASE_DIR, "lista")
PASTA_SAIDA = os.path.join(BASE_DIR, "videos")

os.makedirs(PASTA_SAIDA, exist_ok=True)

for arquivo in os.listdir(PASTA_M3U8):
    if arquivo.endswith(".m3u8"):
        caminho_arquivo = os.path.join(PASTA_M3U8, arquivo)
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        arquivo_saida = os.path.join(PASTA_SAIDA, f"{nome_sem_extensao}.mp4")

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

    
        urls = [linha.strip() for linha in conteudo.splitlines() if linha.startswith("https://")]
        if not urls:
            print(f"Nenhuma URL encontrada em {arquivo}")
            continue

        melhor_url = urls[-1] 

        print(f"Baixando {nome_sem_extensao}...")
        ydl_opts = {
            "outtmpl": arquivo_saida,
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([melhor_url])

        print(f"✅ Vídeo salvo em: {arquivo_saida}")
