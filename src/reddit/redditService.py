import praw

class Reddit:
    def __init__(self):
        self.posts_and_comments = []
        self.top_posts = []

    def accessReddit(self):
        return praw.Reddit("user",
            user_agent="UpvotedUniverse:v0.0.1",
        )

    def getPosts(self):
        reddit = self.accessReddit()
        subreddit = reddit.subreddit('askreddit')
        self.top_posts = subreddit.top(time_filter="day",limit=7)
        
    def getComments(self,post):
        comments = post.comments
        comments.replace_more(limit=0)
        top_comments = comments[:5]
        final_comments= []
        for comment in top_comments:
            comment_dict = {}
            comment_dict['body'] = comment.body
            try:
                comment_dict['author'] = comment.author.name
            except AttributeError:
                comment_dict['author'] = "unknown"
            comment_dict['id'] = comment.id
            final_comments.append(comment_dict)
        
        return final_comments

    def generateDictionary(self):
        for post in self.top_posts:
            post_dict = {}
            post_dict['over_18'] = post.over_18
            post_dict['title'] = post.title
            post_dict['author'] = post.author.name
            post_dict['id'] = post.id
            post_dict['url'] = post.url
            post_dict['comments'] = self.getComments(post)
            self.posts_and_comments.append(post_dict)


    def filterNSFW(self):
        for post in self.posts_and_comments:
            if post['over_18'] is True:
                self.posts_and_comments.remove(post)
    
    def runRedditService(self):
        self.getPosts()
        self.generateDictionary()
        self.filterNSFW()
