from pydub import AudioSegment

def convert_m4a_to_wav(input_path: str, output_path: str):
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio.export(output_path, format="wav")

if __name__ == "__main__":
    input_path = "/home/matheus/desafio-teia/audio_matheus.m4a"  # Caminho correto do arquivo
    output_path = "/home/matheus/desafio-teia/audio_matheus.wav"
    convert_m4a_to_wav(input_path, output_path)
    print(f"Arquivo convertido e salvo em: {output_path}")
