# jeopardyChatBot
A chat bot which answers your questions based on the jeopardy data set

Dataset Location - https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/

tf-idf is used to determine the closest match to the question and the answered from that.

# Requirments
 -NLTK
 -Jupyter
 -Pandas
 -Numpy
 -Python 3

# Files

Download the dataset file into the cloned folder and run the notebook.
The file dataLoader creates a npy file containg  a clean represention of the json with only questions and answers.The questions which contain links filtered out.(Since this file contains questions which have links to the images asked during the show).
