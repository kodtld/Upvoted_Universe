## Upvoted Universe

Upvoted Universe is a powerful program that combines the functionality of several Python libraries to scrape Reddit posts, generate voiceovers using gTTS (Google Text-to-Speech), manipulate screenshots with Selenium, overlay them onto a background video using MoviePy, and even upload the resulting content as reels to Instagram using Selenium. This program is designed to provide a streamlined workflow for creating engaging multimedia content based on popular Reddit posts. It automates the process of gathering relevant information from Reddit, converting text to speech, creating visually appealing video clips, and uploading them to Instagram, saving you time and effort.

### Features

Upvoted Universe offers the following features:

- **Reddit Scraper**: Utilizes the PRAW (Python Reddit API Wrapper) library to scrape Reddit posts based on specified criteria such as subreddit, keywords, or sorting options.
- **Text-to-Speech**: Employs the gTTS library to convert text content from Reddit posts into natural-sounding voiceovers.
- **Screenshot Generation**: Uses Selenium to capture screenshots of web pages related to chosen Reddit posts, such as article pages or external content.
- **Video Composition**: Combines the generated voiceover with screenshots, overlaying them onto a background video using the MoviePy library to create visually appealing clips.
- **Instagram Reels Uploader**: Leverages Selenium to automate the process of uploading the created video clips as Instagram Reels, allowing for easy distribution and engagement on the platform.

### Installation

To install Upvoted Universe, follow these steps:

1. Clone the repository to your local machine or download the source code as a ZIP file and extract it.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to install the project dependencies using Poetry:

```
poetry install
```
