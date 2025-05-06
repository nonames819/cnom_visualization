import numpy as np
import imageio
import os

fps = 30
duration = 3  
total_frames = fps * duration
height, width = 256, 256
video_name = "noise.mp4"

with imageio.get_writer(video_name, fps=fps) as video_writer:
    for _ in range(total_frames):
        frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        
        video_writer.append_data(frame)
