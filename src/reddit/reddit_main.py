import praw

def accessReddit():
    return praw.Reddit("user",
        user_agent="my user agent",
    )   

def getPosts():
    reddit = accessReddit()
    subreddit = reddit.subreddit('askreddit')
    top_posts = subreddit.top(time_filter="day",limit=5)
    return top_posts

def getComments(top_posts):
    for post in top_posts:
        print(f'Title: {post.title}')
        print(f'Author: {post.author.name}')
        print(f'Score: {post.score}')
        print(f'URL: {post.url}')
        print(f'Comments:')
        comments = post.comments
        comments.replace_more(limit=0)  # replace any "load more comments"
        top_comments = comments[:5]  # get the top 5 comments
        for comment in top_comments:
            print(f'   {comment.body}')

def generateContent():
    getComments(getPosts())

generateContent()