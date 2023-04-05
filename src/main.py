from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter

if __name__ == "__main__":
    r = Reddit()
    r.run_reddit_service()
    for post in r.posts_and_comments:
        post_url = post['url']
        post_id = post['id']
        post_comments = post['comments']
        ss = ScreenShotter(post_url, post_id, post_comments)
        ss.run_screenshot_service()