# Upvoted Universe <br>[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/upvoteduniverse/)


Upvoted Universe is a program that combines the functionality of several Python libraries to scrape Reddit posts, generate voiceovers using gTTS (Google Text-to-Speech), manipulate screenshots with Selenium, overlay them onto a background video using MoviePy, and even upload the resulting content as reels to Instagram using Selenium. This program is designed to provide a streamlined workflow for creating engaging multimedia content based on popular Reddit posts. It automates the process of gathering relevant information from Reddit, converting text to speech, creating visually appealing video clips, and uploading them to Instagram, saving you time and effort.

## Features

Upvoted Universe offers the following features:

- **Reddit Scraper**: Utilizes the PRAW (Python Reddit API Wrapper) library to scrape Reddit posts based on specified criteria such as subreddit, keywords, or sorting options.
- **Text-to-Speech**: Employs the gTTS library to convert text content from Reddit posts into natural-sounding voiceovers.
- **Screenshot Generation**: Uses Selenium to capture screenshots of web pages related to chosen Reddit posts, such as article pages or external content.
- **Video Composition**: Combines the generated voiceover with screenshots, overlaying them onto a background video using the MoviePy library to create visually appealing clips.
- **Instagram Reels Uploader**: Leverages Selenium to automate the process of uploading the created video clips as Instagram Reels, allowing for easy distribution and engagement on the platform.

## Installation

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

## Before Usage

Before using Upvoted Universe, make sure you have the following prerequisites and files set up:

1. **Background Videos**: Ensure that you have landscape format background videos in the `src/resources/bg_videos/` directory. These videos will be used as the background for the generated clips. Make sure the videos are compatible with the desired output format.

2. **Geckodriver**: Place the `geckodriver` executable in the `src/drivers/` directory. Geckodriver is required for Selenium to interact with the Firefox web browser. Ensure that the version of Geckodriver matches your Firefox browser version.

3. **Converted Videos Database**: In the `src/` directory, you should have a file named `converted_videos.db`. This SQLite database file is used by Upvoted Universe to keep track of the converted videos and their associated information. If the file does not exist, the program will create it automatically during runtime.

Make sure to set up the above prerequisites and files correctly to ensure smooth execution of Upvoted Universe.
