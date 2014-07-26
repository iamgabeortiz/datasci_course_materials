import sys
import json
import re


def main():
    if len(sys.argv) < 3:
        sent_file = open("AFINN-111.txt")
        tweet_file = open("output.txt")
    else:
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])

    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweet_data = {}  # initialize an empty dictionary
    tweet_place = {}  # initialize an empty dictionary
    tweets = []  # initialize an empty list
    state_score = {}  # initialize an empty dictionary
    final_state_score = {}  # initialize an empty dictionary
    for line in tweet_file:
        tweet_data = json.loads(line)
        if tweet_data.get("place") and tweet_data["place"]["country_code"] == "US":
            try:
                tweet_place = tweet_data["place"]["full_name"].encode("utf8").split(", ")  # store tweet state
            except KeyError:
                continue
            if tweet_place[1] != "USA":
                tweets = tweet_data["text"].encode("utf-8").lower()  # store tweet text
                sent_score = 0  # initialize zero value sentiment score variable for each tweet
                for words in tweets.split():
                    strip_word = re.sub('[^0-9a-zA-Z]+', '', words)  # filter non alphanumeric characters
                    if strip_word in scores:
                        sent_score += scores[strip_word]  # store the aggregate sum of any scores
                state_score[tweet_place[1]] = sent_score  # store state and score for each tweet
    print state_score
    for state, score in state_score.items():
        temp = sum(score) / len(score)
        final_state_score[state] = temp

    print max(final_state_score, key=final_state_score.get)

if __name__ == '__main__':
    main()
