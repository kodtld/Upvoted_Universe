from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter

if __name__ == "__main__":
    r = Reddit()
    r.run_reddit_service()
    for post in r.posts_and_comments:
        ss = ScreenShotter()
        ss.login_reddit()
        post_url = post['url']
        post_id = post['id']
        
        ss.title_screenshot(post_url, post_id)
        ss.close_driver()