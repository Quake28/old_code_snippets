import requests_with_caching
import json


def get_movies_from_tastedive(title):
    string = "https://tastedive.com/api/similar"
    parameters = {"q": title, "type": "movies", "limit": "5"}
    x = requests_with_caching.get(string, params=parameters)
    return x.json()


def extract_movie_titles(dictx):
    y = []
    for a in dictx["Similar"]["Results"]:
        y.append(a["Name"])
    return y


def get_related_titles(list1):
    list2 = []
    for a in list1:
        dictx = get_movies_from_tastedive(a)
        for b in extract_movie_titles(dictx):
            if b not in list2:
                list2.append(b)
    return list2


def get_movie_data(title):
    urlString = "http://www.omdbapi.com/"
    params1 = {"t": title, "r": "json"}
    x = requests_with_caching.get(urlString, params1)
    # print(x.url)
    return x.json()


def get_movie_rating(dictx):
    for a in dictx["Ratings"]:
        if a["Source"] == "Rotten Tomatoes":
            return int(a["Value"][:2])
    return 0


def get_sorted_recommendations(listx):
    list1 = get_related_titles(listx)
    list2 = sorted(
        list1, key=lambda x: (get_movie_rating(get_movie_data(x)),x), reverse=True
    )
    return list2


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
