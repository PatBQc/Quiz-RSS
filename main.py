import os
import feedparser
from feedgen.feed import FeedGenerator

def add_episode_to_rss(rss_file, title, description, link):
    # Parse the existing RSS file
    if not os.path.exists(rss_file):
        # Create a new RSS feed file
        feed = feedparser.FeedParserDict()
        feed.feed = {
            'title': 'My RSS Feed',
            'link': 'https://example.com/rss',
            'description': 'This is my RSS feed'
        }
        feed.entries = []
    else:
        # Parse the existing RSS file
        feed = feedparser.parse(rss_file)

    # Create a new entry for the episode
    new_entry = {
        'title': title,
        'description': description,
        'link': link
    }

    # Append the new entry to the existing entries
    feed.entries.append(new_entry)

    # Save the modified RSS file
    fg = FeedGenerator()
    fg.title(feed.feed['title'])
    fg.link(href=feed.feed['link'])
    fg.description(feed.feed['description'])

    for entry in feed.entries:
        fe = fg.add_entry()
        fe.title(entry['title'])
        fe.description(entry['description'])
        fe.link(href=entry['link'])

    with open(rss_file, 'w+', encoding='utf-8') as file:
        rss_str = fg.rss_str(pretty=True).decode('utf-8')
        file.write(rss_str)

# Example usage
rss_file = 'rss.xml'
title = 'New Episode'
description = 'This is the description of the new episode.'
link = 'https://example.com/episode123'
add_episode_to_rss(rss_file, title, description, link)