from moviepy.editor import VideoFileClip
import random

class VideoSectionExtractor:
    def __init__(self, section_length):
        randint = random.choice([1,2])
        self.video_path = f'/home/kxsalmi/Upvoted_Universe/src/resources/bg_videos/Video{randint}.mp4'
        self.section_length = section_length

        self.width = 1080
        self.height = 1920

    def extract_section(self):
        clip = VideoFileClip(self.video_path)

        # Get duration of video
        duration = clip.duration

        # Calculate start and end times for desired section
        section_start = random.uniform(0, duration - self.section_length)
        section_end = section_start + self.section_length

        # Extract section
        section = clip.subclip(section_start, section_end)

        # Crop section from center
        w, h = section.size
        x1 = (w - h) // 2
        y1 = 0
        x2 = x1 + h
        y2 = h

        section = section.crop(x1=x1, y1=y1, x2=x2, y2=y2)

        # Resize section to desired dimensions
        section = section.resize((1080, 1920))

        return section
