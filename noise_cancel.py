import noisereduce as nr
import librosa
import soundfile as sf

print("🔊 Loading audio...")
audio, rate = librosa.load("input_audio.wav", sr=None)

print("🔕 Reducing noise...")
cleaned = nr.reduce_noise(y=audio, sr=rate)

print("💾 Saving clean audio...")
sf.write("clean_audio.wav", cleaned, rate)

print("✅ Noise reduced audio saved as clean_audio.wav")
