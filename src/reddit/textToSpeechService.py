import os
from gtts import gTTS

class TextToSpeech():
    def __init__(self, post_body, post_id, post_comments) -> None:
        self.post_id = post_id
        self.post_body = post_body
        self.post_comments = post_comments

    def create_voiceover(self, text, content_id, content_type):
        filePath = f'./resources/voiceovers/{self.post_id}/{content_type}-{content_id}.mp3'
        tts = gTTS(text)
        tts.save(filePath)

    def runTTSService(self):
        new_dir_path = os.path.join(os.getcwd(), 'resources', 'voiceovers', self.post_id)
        os.makedirs(new_dir_path, exist_ok=True)
        self.create_voiceover(self.post_body, self.post_id, "title")
        for comment in self.post_comments:
            self.create_voiceover(comment['body'], comment['id'], "comment")
