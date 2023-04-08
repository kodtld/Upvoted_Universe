import os
import moviepy.editor as mp

class Parser:
    def __init__(self, post_id):
        self.post_id = post_id
        self.image_folder = f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{self.post_id}'
        self.audio_folder = f'/home/kxsalmi/Upvoted_Universe/src/resources/voiceovers/{self.post_id}'
        self.image_files = sorted(os.listdir(self.image_folder))
        self.audio_files = sorted(os.listdir(self.audio_folder))
        self.output_folder = f"/home/kxsalmi/Upvoted_Universe/src/resources/image_and_audio/{self.post_id}"
        os.makedirs(self.output_folder)

    def combine_image_and_audio(self):
        for i, image_file in enumerate(self.image_files):
            audio_file = self.audio_files[i]
            image_path = os.path.join(self.image_folder, image_file)
            audio_path = os.path.join(self.audio_folder, audio_file)
            image = mp.ImageClip(image_path)
            audio = mp.AudioFileClip(audio_path)
            video = image.set_audio(audio)
            video_duration = audio.duration
            final_video = video.subclip(0, video_duration)
            final_video_speed = final_video.speedx(1.25)
            output_path = os.path.join(self.output_folder, f"output_{i}.mp4")
            final_video_speed.write_videofile(output_path, fps=24, codec='libx264')
