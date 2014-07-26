import sys
import json
import re


def main():
    if len(sys.argv) < 2:
        tweet_file = open("output.txt")
    else:
        tweet_file = open(sys.argv[1])

    tweet_data = {}  # initialize an empty dictionary
    tweets = []  # initialize an empty list
    for line in tweet_file:
        tweet_data = json.loads(line)
        try:
            if tweet_data["lang"] == "en":
                # load json text only and convert to lower utf-8
                tweets.append(tweet_data["text"].encode("utf-8").lower())
        except KeyError:
            continue

    terms = {}  # initialize an empty dictionary
    term_count = 0
    for index in range(len(tweets)):
        for words in tweets[index].split():
            term_count += 1  # increment count of total words in all tweets
            strip_word = re.sub('[^0-9a-zA-Z]+', '', words)  # filter non alphanumeric characters
            if strip_word in terms:
                terms[strip_word] += 1  # store word and count
            else:
                terms[strip_word] = 1

    for x in terms:
        print x, terms[x]

if __name__ == '__main__':
    main()
