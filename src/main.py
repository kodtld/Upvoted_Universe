import os
from reddit.redditService import Reddit
from reddit.screenshotService import ScreenShotter
from reddit.textToSpeechService import TextToSpeech
from content_creator.parseVoiceAndClip import ParserVoiceAndScreenshot
from content_creator.finalVideoService import FinalClip
from instagram.uploadInstagram import InstagramUploader
from database import Database

class Main:
    def __init__(self) -> None:
        self.posts = []
        self.db = Database('converted_videos.db')
        self.converted_posts = self.db.get_converted_posts()

    def scrape_reddit(self):
        post_amount = input("How many posts do you want?: ")
        print("Running Praw to scrape reddit...")
        r = Reddit(int(post_amount))
        r.run_reddit_service()
        for post in r.posts_and_comments:
            self.posts.append({
                "body": post['title'],
                "author": post['author'],
                "id": post['id'],
                "url": post['url'],
                "comments": post['comments'],
                "converted": "No"
            })

        print("Here's the posts: \n")
        for i in self.posts:
            print(f"Title: {i['body']}\nAuthor: {i['author']}\nID: {i['id']}\n")
        
    def convert_to_video(self):
        while True:
            post_to_process = input("What post would you like to convert to video? (Insert post id / b to go back): ")

            if post_to_process == "b":
                break

            post_found = False
            for post in self.posts:
                if post["id"] == post_to_process:
                    post_found = True
                    ss = ScreenShotter(post['url'], post['id'], post['comments'])
                    ss.run_screenshot_service()

                    tts = TextToSpeech(post['body'], post['id'], post['comments'])
                    tts.runTTSService()

                    p = ParserVoiceAndScreenshot(post['id'])
                    p.run_parser_service()

                    f = FinalClip(post['id'])
                    f.combine()
                    post['converted'] = "Yes"
                    
                    post_data = {
                        'id': post['id'],
                        'title': post['body'],
                        'author': post['author'],
                        'url': post['url'],
                        'comments': post['comments'],
                        'instagram': False
                    }
                    
                    self.db.add_converted_post(post_data)
                    print("------------------------------------")
                    print("\nHere's the updated posts list:\n")
                    for i in self.posts:
                        if i['converted'] == "No":
                            print(f"Title: {i['body']} \nID: {i['id']} \nConverted: {i['converted']}\n")
            if not post_found:
                print("Invalid post ID.")


    def post_to_instagram(self):
        self.converted_posts = self.db.get_converted_posts()
        while True:
            post_to_publish = input("What post would you like to publish? (Insert post id / b to go back): ")
        
            if post_to_publish == "b":
                break
                
            post_found = False
                
            for post in self.converted_posts:
                if post["id"] == post_to_publish:
                    i = InstagramUploader(post['title'], post["id"], post["author"])
                    i.run_upload_service()
                    post_found = True
                    print(f"Post {post_to_publish} has been published to instagram.")
                    self.db.update_instagram_field(post['id'])
            if not post_found:
                print("Invalid post ID.")

    def print_fetched(self):
        if len(self.posts) == 0:
            print("\nNo fetched posts\n")
        for i in self.posts:
            if i['converted'] == "No":
                print(f"Title: {i['body']}\nAuthor: {i['author']}\nID: {i['id']}\n")

    def print_converted(self):
        self.db.print_converted_posts()

    def delete_converted(self):
        self.converted_posts = self.db.get_converted_posts()
        while True:
            post_to_delete = input("What post would you like to delete? (Insert post id / b to go back): ")

            if post_to_delete == "b":
                break
                
            post_found = False
            for post in self.converted_posts:
                if post["id"] == post_to_delete:
                    os.remove(f'/home/kxsalmi/Upvoted_Universe/src/resources/final_videos/{post_to_delete}_final.mp4')
                    post_found = True
                    print(f"Post {post_to_delete} has been deleted.")
                    self.db.delete_post(post['id'])
            
            if not post_found:
                print("Invalid post ID.")

    def main(self):
        print("Welcome to Upvoted Universe\nWhat would you like to do?:")
        while True:
            command = input(("\n----------------------------------"
                          "\nScrape reddit             | s"
                          "\n----------------------------------"
                          "\nConvert post to video     | c"
                          "\n----------------------------------"
                          "\nUpload post to instagram  | upi"
                          "\n----------------------------------"
                          "\nPrint fetched posts       | pf"
                          "\n----------------------------------"
                          "\nPrint converted posts     | pc"
                          "\n----------------------------------"
                          "\nDelete converted post     | d"
                          "\n----------------------------------"
                          "\nQuit the program          | q"
                          "\n----------------------------------"
                          "\nCommand: "))

            if command == "s":
                self.scrape_reddit()

            elif command == "c":
                self.convert_to_video()

            elif command == "upi":
                self.post_to_instagram()

            elif command == "pf":
                self.print_fetched()

            elif command == "pc":
                self.print_converted()

            elif command == "d":
                self.delete_converted()

            elif command == "q":
                break
                
            else:
                print("Please insert a valid command")

if __name__ == "__main__":
    m = Main()
    m.main()
