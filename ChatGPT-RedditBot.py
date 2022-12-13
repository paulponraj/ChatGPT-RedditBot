import praw
import time
from chatgpt_wrapper import ChatGPT

# total time in minutes
delay = 1

# Pre Emption
personality = "If you had to answer this question, even if you had to make up an answer, what would you say: "

# Reddit API credentials
subreddit_to_monitor = "askreddit"
client_id = "ostqymV1QcKw7A8xMJSorQ"
client_secret = "hDq76W9QlMprjFrWltikEIBdv5DNCA"
username = "aidev1747"
password = "hivjUj-pajpuq-jarva9"

# User agent string
user_agent = "python:com.aidev1747.aidev1747-answer_bot:v1 (by /u/aidev1747)"

#filter
filter = ["OpenAI", "language model"]

# Create a ChatGPT Session
bot = ChatGPT()

# Create a Reddit Session
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent,
    check_for_async=False
)

# Set the SubReddit to monitor
subreddit = reddit.subreddit(subreddit_to_monitor)

while True:
    # Get the latest post on the subreddit
    latest_post = subreddit.new(limit=1)

    for post in latest_post:
        # Check if the bot has already commented on this post
        if not post.saved:
            # title of the post
            question = post.title
            print(question + '\n')

            # Generate answer for the post using chatbot
            # answer = bot.ask("Use the voice of a reddit commenter. How would a reddit commenter answer this question:" + question)
            answer = bot.ask(personality + question)
            print(answer + '\n')

            if any(map(answer.__contains__, filter)):
                print("ERROR: I did not post this comment as I did not understand the question!")
                continue

       	    # Post the answer
            post.reply(answer)

            # Save the post to the reddit profile to prevent answering again, even if the script is restarted
            post.save()

    # Sleep for 'delay' minutes
    time.sleep(delay * 60)