from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter

if __name__ == "__main__":
    r = Reddit()
    r.runRedditService()
    for post in r.posts_and_comments:
        post_url = post['url']
        post_id = post['id']
        ss = ScreenShotter(post_url, post_id)
        ss.titleScreenshot()