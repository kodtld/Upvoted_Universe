from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter
from content_creator.textToSpeechService import TextToSpeech

if __name__ == "__main__":
    r = Reddit()
    r.run_reddit_service()
    for post in r.posts_and_comments:
        post_url = post['url']
        post_id = post['id']
        post_comments = post['comments']
        post_body = post['title']
        ss = ScreenShotter(post_url, post_id, post_comments)
        ss.run_screenshot_service()

        tts = TextToSpeech(post_body, post_id, post_comments)
        tts.runTTSService()    
