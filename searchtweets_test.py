# Sue Huang
# 01/04/2019
# Searches Twitter for clouds taste and compiles results into a text file

from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results, convert_utc_time

#load credentials
premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                      yaml_key="search_tweets_premium",
                                      env_overwrite=False)

#search term
#twitter_text1 = clouds tastes like
#twitter_text2 = clouds taste like
rule = gen_rule_payload("clouds taste like", results_per_call=500, from_date="2007-01-01", to_date="2008-01-01") #min 10, max 100 results; min 10, max 500 for paid
print(rule)

#search with max_results (maximum number of tweets or counts to return from)
tweets = collect_results(rule,
                        max_results=500,
                        result_stream_args=premium_search_args)

#output
#[print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]];

#convert to string
tweet_str = ""

for tweet in tweets[0:500]: #variable number
    tweet_str += str(tweet.all_text)     
print(tweet_str)

#write to file in append mode
file = open("twitter_text2.txt", "a")
file.write(tweet_str)
#file.write(str((tweets[1]).all_text))
file.close()
