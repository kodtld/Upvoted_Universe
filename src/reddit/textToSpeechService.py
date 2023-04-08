import os
from gtts import gTTS

class TextToSpeech():
    def __init__(self, post_body, post_id, post_comments) -> None:
        self.post_id = post_id
        self.post_body = post_body
        self.post_comments = post_comments

    def create_voiceover(self, text, content_id, content_type):
        filePath = f'/home/kxsalmi/Upvoted_Universe/src/resources/voiceovers/{self.post_id}/{content_type}-{content_id}.mp3'
        tts = gTTS(text)
        tts.save(filePath)

    def runTTSService(self):
        os.makedirs(f'/home/kxsalmi/Upvoted_Universe/src/resources/voiceovers/{self.post_id}')
        self.create_voiceover(self.post_body, self.post_id, "title")
        for comment in self.post_comments:
            self.create_voiceover(comment['body'], comment['id'], "comment")
