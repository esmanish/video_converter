import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("video.mov") #include your location of your video with the video extension here.
clip.write_videofile("output.mp4") # output video name and the extension to which you want to convert your video.
