# 🎧 Noise Cancellation for Video (Offline, No API)

This project removes background noise from any video using FFmpeg + AI-based Python denoising.

---

## 💻 How It Works:
1. Extract audio from video (using `ffmpeg`)
2. Use ML to reduce noise (`noisereduce` library)
3. Merge clean audio back into the original video

---

## 🔧 Setup
```bash
git clone https://github.com/yourusername/noise-cancel-video.git
cd noise-cancel-video
pip install -r requirements.txt
