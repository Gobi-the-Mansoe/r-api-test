import praw
from reddit_objects import Reddit

def main():
    # client_id = config['REDDITAPI']['client_id']
    # client_secret = config['REDDITAPI']['client_secret']
    # username = config['REDDITAPI']['username']
    # password = config['REDDITAPI']['password']
    # user_agent = config['REDDITAPI']['user_agent']
    # reddit = initialize_instance(client_id, client_secret, username, password, user_agent)
    # subreddit = reddit.subreddit('futurology')
    # hot_futurology = subreddit.hot(limit=5)
    reddit = Reddit()
    for post in reddit.get_hot_posts():
        if not post.stickied:
            print(f'Title: {post.title}, Ups: {post.ups}, Downs: {post.downs}')



def initialize_instance(client_id, client_secret, username, password, user_agent):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)
    return reddit


if __name__ == '__main__':
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')
    main()
