---

### ✅ 3. `extract_audio.sh`
```bash
ffmpeg -i input_video.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 input_audio.wav
