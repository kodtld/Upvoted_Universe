# Upvoted Universe <br>[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/upvoteduniverse/)

<img src="https://github.com/kodtld/Upvoted_Universe/blob/main/example.gif" alt="Image" height="400" />
<br>
Upvoted Universe is a program that combines the functionality of several Python libraries to scrape Reddit posts, generate voiceovers using gTTS (Google Text-to-Speech), manipulate screenshots with Selenium, overlay them onto a background video using MoviePy, and even upload the resulting content as reels to Instagram using Selenium. This program is designed to provide a streamlined workflow for creating engaging multimedia content based on popular Reddit posts. It automates the process of gathering relevant information from Reddit, converting text to speech, creating visually appealing video clips, and uploading them to Instagram, saving you time and effort.

## Features

Upvoted Universe offers the following features:

- **Reddit Scraper**: Utilizes the PRAW (Python Reddit API Wrapper) library to scrape Reddit posts based on specified criteria such as subreddit, keywords, or sorting options.
- **Text-to-Speech**: Employs the gTTS library to convert text content from Reddit posts into natural-sounding voiceovers.
- **Screenshot Generation**: Uses Selenium to capture screenshots of web pages related to chosen Reddit posts, such as article pages or external content.
- **Video Composition**: Combines the generated voiceover with screenshots, overlaying them onto a background video using the MoviePy library to create visually appealing clips.
- **Instagram Reels Uploader**: Leverages Selenium to automate the process of uploading the created video clips as Instagram Reels, allowing for easy distribution and engagement on the platform.

## Before Usage

Before using Upvoted Universe, make sure you have the following prerequisites and files set up:

1. **Background Videos**: Ensure that you have landscape format background videos in the `src/resources/bg_videos/` directory. These videos will be used as the background for the generated clips. Make sure the videos are compatible with the desired output format.

2. **Geckodriver**: Place the `geckodriver` executable in the `src/drivers/` directory. Geckodriver is required for Selenium to interact with the Firefox web browser. Ensure that the version of Geckodriver matches your Firefox browser version.

3. **Converted Videos Database**: In the `src/` directory, you should have a file named `converted_videos.db`. This SQLite database file is used by Upvoted Universe to keep track of the converted videos and their associated information. If the file does not exist, the program will create it automatically during runtime.

4. **Environment Variables**: Create a `.env` file in the root of the project directory and provide the following details in the file:
- **REDDIT_CLIENT_ID**=your_reddit_client_id
- **REDDIT_SECRET**=your_reddit_secret
- **REDDIT_USERNAME**=your_reddit_username
- **REDDIT_PASSWORD**=your_reddit_password
- **REDDIT_REDIRECT_URL**=your_reddit_redirect_url
- **INSTAGRAM_USERNAME**=your_instagram_username
- **INSTAGRAM_PASSWORD**=your_instagram_password

For the REDDIT_CLIENT_ID, REDDIT_SECRET, and REDDIT_REDIRECT_URL, please refer to the [Reddit API documentation](https://www.reddit.com/dev/api/) to obtain the necessary credentials for authentication.

## Installation & Running

To install Upvoted Universe, follow these steps:

1. Clone the repository to your local machine or download the source code as a ZIP file and extract it.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to install the project dependencies using Poetry:

```
poetry install
```
4. Once the installation is complete, activate the Poetry virtual environment:
```
poetry shell
```
5. Once poetry is activated, run the program from src directory with:
```
python3 main.py
```
## User Manual

The Upvoted Universe program provides several commands to perform various actions. Once the program is running, you can interact with it using the following commands:

- **Scrape Reddit**: Use the command `s` to scrape Reddit and fetch new posts.

- **Convert Post to Video**: Use the command `c` to convert a specific post to a video clip. You will be prompted to enter the post ID or URL.

- **Upload Post to Instagram**: Use the command `upi` to upload a converted post as an Instagram reel. You will be prompted to enter the post ID or URL.

- **Print Fetched Posts**: Use the command `pf` to print the fetched Reddit posts along with their details.

- **Print Converted Posts**: Use the command `pc` to print the converted posts along with their details.

- **Delete Converted Post**: Use the command `d` to delete a converted post. You will be prompted to enter the post ID or URL.

- **Quit the Program**: Use the command `q` to quit the program. The program also deletes temporary voiceover- and video files when it's quit. (Doesn't affect converted final videos)

Please note that you can enter the commands directly into the program's command-line interface to perform the desired actions.
