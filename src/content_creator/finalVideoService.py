import os
import moviepy.editor as mp
from content_creator.backgroundService import VideoSectionExtractor

class FinalClip:
    def __init__(self, post_id):
        self.post_id = post_id
        self.clip2_path = f'./resources/image_and_audio/{self.post_id}/final_output.mp4'
        self.clip2 = mp.VideoFileClip(self.clip2_path).set_opacity(0.95)
        video_extractor = VideoSectionExtractor(self.clip2.duration)
        self.clip1 = video_extractor.extract_section()
        self.output_folder = './resources/final_videos/'
        
    def combine(self):
        clip1_audio = self.clip1.audio.volumex(0.2)
        self.clip1 = self.clip1.set_audio(clip1_audio)

        final_clip = mp.CompositeVideoClip([self.clip1, self.clip2.set_position("center")], size=self.clip1.size)

        output_path = os.path.join(self.output_folder, f'{self.post_id}_final.mp4')
        final_clip.write_videofile(output_path, codec='libx264')
