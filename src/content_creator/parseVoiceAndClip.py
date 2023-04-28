import os
import moviepy.editor as mp

class ParserVoiceAndScreenshot:
    def __init__(self, post_id, max_length=60):
        self.post_id = post_id
        self.image_folder = f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{self.post_id}'
        self.audio_folder = f'/home/kxsalmi/Upvoted_Universe/src/resources/voiceovers/{self.post_id}'
        self.output_folder = f"/home/kxsalmi/Upvoted_Universe/src/resources/image_and_audio/{self.post_id}"
        self.image_files = sorted(os.listdir(self.image_folder))
        self.audio_files = sorted(os.listdir(self.audio_folder))
        self.ultimate_duration = 0
        self.ultimate_clip_count = 0
        self.max_length = max_length

    def combine_image_and_audio(self):
        os.makedirs(self.output_folder)
        for i, image_file in enumerate(self.image_files):
            audio_file = self.audio_files[i]
            image_path = os.path.join(self.image_folder, image_file)
            audio_path = os.path.join(self.audio_folder, audio_file)
            image = mp.ImageClip(image_path)
            audio = mp.AudioFileClip(audio_path)
            image = image.resize(width=950)
            video = image.set_audio(audio)
            video_duration = audio.duration
            final_video = video.subclip(0, video_duration)

            final_video_speed = final_video.speedx(1.30)
            output_path = os.path.join(self.output_folder, f"output_{i}.mp4")
            final_video_speed.write_videofile(output_path, fps=60, codec='libx264')

    def concatenate_clips(self):
        video_files = [os.path.join(self.output_folder, file) for file in sorted(os.listdir(self.output_folder))]
        output_path = os.path.join(self.output_folder, "final_output.mp4")
        clips = []
        for file in reversed(video_files):
            clip = mp.VideoFileClip(file)
            if self.check_length(clip):
                clips.append(clip)
            os.remove(file)
            
        for i in range(len(clips)-1):
            clips[i] = clips[i].audio_fadeout(1)
    
        if self.ultimate_clip_count > 1:
            final_clip = mp.concatenate_videoclips(clips, method='compose').set_fps(60)
            final_clip.write_videofile(output_path, codec='libx264')

    def check_length(self, clip):
        if self.ultimate_duration + clip.duration <= float(self.max_length):
            self.ultimate_duration += clip.duration
            self.ultimate_clip_count += 1
            return True

        return False

    def run_parser_service(self):
        self.combine_image_and_audio()
        self.concatenate_clips()