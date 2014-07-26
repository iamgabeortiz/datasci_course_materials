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

    tweet_data = {}
    tweets = []  # initialize an empty list
    for line in tweet_file:
        tweet_data = json.loads(line)
        try:
            if tweet_data["lang"] == "en":
                # load json text only and convert to lower utf-8
                tweets.append(tweet_data["text"].encode("utf-8").lower())
        except KeyError:
            continue

    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    terms = []  # initialize an empty list
    noscores = {}  # initialize an empty dictionary
    for index in range(len(tweets)):
        temp_score = 0
        for words in tweets[index].split():
            if words in scores:
                temp_score += scores[words]
            elif words not in terms:
                terms.append(words)
        #sent_score.append(temp_score)  # store the aggregate sum of any scores for each tweet
        for words2 in tweets[index].split():
            strip_word = re.sub('[^0-9a-zA-Z]+', '', words2)  # filter non alphanumeric characters
            if strip_word in terms:
                noscores[strip_word] = temp_score

    for x in noscores:
        print x, noscores[x]

if __name__ == '__main__':
    main()
