ffmpeg -i input_video.mp4 -i clean_audio.wav -c:v copy -map 0:v:0 -map 1:a:0 -shortest final_output.mp4
