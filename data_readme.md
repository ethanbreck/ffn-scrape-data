# README for Data folder

## Users folder

For the user folder, it contains the User ID, and the story ids for the stories they have hit favorite on. There is no story metadata in those files, just the following information in the following format:

[
'User_id' = 1342,
'date_scraped' = ~numerical value for date~,
'Favorites' = [
id 1,
id 2,
id 3,
id 4            ]
]

The name of the favorite file is the userid.json, and there is one for each user, after user 60k, as its a feature i added after 60k users.

## HTML folder

For the HTML folder, that is the full content from the website, in case i need to re-scrape information, or someone else wants to do something. Like the Favorites, its a feature added after user 60k.

## StoryMeta folder

For the storymeta folder, that was the core of this program. To scrape story metadata. Currently there are just the individual story files, with the name formatted as story_id.json.

The information in that file is as follows:

-id: the id of the story
-canon_type: the type of canon
-canon: the name of the canon
-author_id: the user id of the author
-title: the title of the story
-updated: the timestamp of the last time the story was updated
-published: the timestamp of when the story was originally published
-lang: the language the story is written in
-genres: a list of the genres that the author categorized the story as
-num_reviews
-num_favs
-num_follows
-num_words: total number of words in all chapters of the story
-rated: the story's rating.
