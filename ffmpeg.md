ffmpeg -i .\multiple_trials.mp4 -vframes 1 out.png

ffmpeg -i input.mp4 -filter:v "crop=w:h:x:y" output.mp4

ffmpeg -y -i .\multiple_trials_crop.mp4 -filter_complex "fps=15,split[v1][v2]; [v1]palettegen=stats_mode=full [palette]; [v2][palette]paletteuse=dither=sierra2_4a" -vsync 0 output.gif