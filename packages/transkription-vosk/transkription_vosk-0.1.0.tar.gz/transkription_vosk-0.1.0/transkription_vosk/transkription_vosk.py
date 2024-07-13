#!/usr/bin/env python3

import os
import sys
import wave
import json
import argparse
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

def transcribe_audio(input_file, model_path, output_file):
    # Konvertieren Sie die Audiodatei in eine WAV-Datei mit 16kHz und mono
    print("Lade und konvertiere Audiodatei...")
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export("temp_audio.wav", format="wav", parameters=["-acodec", "pcm_s16le"])
    print("Konvertierung abgeschlossen.")

    # Überprüfen Sie das Format der konvertierten Datei
    print("Überprüfe das Format der konvertierten Datei...")
    with wave.open("temp_audio.wav", "rb") as wf:
        channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        print(f"Kanalanzahl: {channels}, Abtastbreite: {sampwidth}, Abtastrate: {framerate}")

        if channels != 1 or sampwidth != 2 or framerate != 16000:
            print("Audio muss im WAV-Format mit 16kHz, mono sein")
            sys.exit()
    print("Formatüberprüfung abgeschlossen.")

    # Laden Sie das Vosk-Modell
    print("Lade das Vosk-Modell...")
    if not os.path.exists(model_path):
        print("Das Modellverzeichnis existiert nicht")
        sys.exit()
    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)
    print("Modell geladen.")

    # Öffnen Sie die WAV-Datei erneut
    with wave.open("temp_audio.wav", "rb") as wf:
        # Transkribieren Sie die Audiodaten
        print("Beginne mit der Transkription...")
        transcription = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                transcription += json.loads(result)["text"] + " "

        # Letztes Ergebnis
        final_result = rec.FinalResult()
        transcription += json.loads(final_result)["text"]
        print("Transkription abgeschlossen.")

    # Schreiben Sie die Transkription in die Ausgabedatei
    print("Schreibe Transkription in die Ausgabedatei...")
    with open(output_file, "w") as f:
        f.write(transcription.strip())
    print(f"Transkription gespeichert in: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Transkription einer Audiodatei mit Vosk.")
    parser.add_argument("-i", "--input", required=True, help="Pfad zur Eingabe-Audiodatei (z.B. .ogg, .mp3, .wav, .flac)")
    parser.add_argument("-v", "--voice_model", required=True, help="Pfad zum Vosk-Sprachmodell")
    parser.add_argument("-o", "--output", required=True, help="Pfad zur Ausgabe-Textdatei")

    args = parser.parse_args()

    transcribe_audio(args.input, args.voice_model, args.output)

if __name__ == "__main__":
    main()