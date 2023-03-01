# Public Datasets

Natural Language Processing (NLP) is about (raw) unstructed textual data

1. https://elitedatascience.com/datasets#nlp - Datasets for Data Science and Machine Learning.
2. https://github.com/niderhoff/nlp-datasets - List of unstructured text data.
3. https://cseweb.ucsd.edu/~jmcauley/datasets.html - This page contains a collection of datasets that have been collected for research on Recommender Systems and Personalization Datasets.

# Sample datasets for baseline experiments
1. [Twenty Newsgroups](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) - The 20 Newsgroups data set is a collection of approximately 20,000 newsgroup documents, partitioned (nearly) evenly across 20 different newsgroups. Great for practicing text classification.
   * <b>from sklearn.datasets import fetch_20newsgroups</b>
   * See also http://qwone.com/~jason/20Newsgroups/
3. [IMDB movies reviews dataset](http://ai.stanford.edu/~amaas/data/sentiment/) - This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. Authors provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing.
4. [Twitter Sentiment140](http://help.sentiment140.com/for-students) - Sentiment140 was created by Alec Go, Richa Bhayani, and Lei Huang and is a popular dataset, which uses 1,600,000 tweets with emoticons pre-removed.
5. [NLTK-Movie Reviews](https://www.nltk.org/_modules/nltk/corpus/reader/reviews.html) - A small dataset colleced by Bing and Liu, with 2000 reviews. This dataset is great for practicing sentiment classification.
   * <b>from nltk.corpus import movie_reviews</b>
