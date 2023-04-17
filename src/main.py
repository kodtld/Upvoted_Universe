from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter
from reddit.textToSpeechService import TextToSpeech
from content_creator.parseVoiceAndClip import ParserVoiceAndScreenshot
from content_creator.finalVideoService import FinalClip
from instagram.uploadInstagram import InstagramUploader

if __name__ == "__main__":
    r = Reddit()
    r.run_reddit_service()
    for post in r.posts_and_comments:
        post_body = post['title']
        post_id = post['id']
        post_url = post['url']
        post_comments = post['comments']
        post_author = post['author']

        ss = ScreenShotter(post_url, post_id, post_comments)
        ss.run_screenshot_service()

        tts = TextToSpeech(post_body, post_id, post_comments)
        tts.runTTSService()

        p = ParserVoiceAndScreenshot(post_id)
        p.run_parser_service()
    
        f = FinalClip(post_id)
        f.combine()

        i = InstagramUploader(post_id, post_author)
        i.run_screenshot_service()