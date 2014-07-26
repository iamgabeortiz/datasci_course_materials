import sys
import json


def main():
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("output.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line)["text"].lower())  # load json text only and convert to lowercase
        except KeyError:
            continue

    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for index in range(len(tweets)):
        sent_score = 0  # initialize zero value sentiment score variable for each tweet
        for words in tweets[index].split():
            if words in scores:
                sent_score += scores[words]  # store the aggregate sum of any scores
        print sent_score  # print sentiment score to stdout

if __name__ == '__main__':
    main()
