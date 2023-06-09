import os
from moviepy.editor import VideoFileClip
import random

class VideoSectionExtractor:
    def __init__(self, section_length):
        video_directory = './resources/bg_videos/'
        self.video_files = []
        for filename in os.listdir(video_directory):
            if filename.endswith('.mp4'):
                print(os.path.join(video_directory, filename))
                self.video_files.append(os.path.join(video_directory, filename))
        self.video_path = random.choice(self.video_files)
        self.section_length = section_length

        self.width = 1080
        self.height = 1920

    def extract_section(self):
        clip = VideoFileClip(self.video_path)
        duration = clip.duration
        section_start = random.uniform(0, duration - self.section_length)
        section_end = section_start + self.section_length
        section = clip.subclip(section_start, section_end)

        w, h = section.size
        x1 = (w - h) // 2
        y1 = 0
        x2 = x1 + h
        y2 = h
        section = section.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        section = section.resize((1080, 1920))
        return section
