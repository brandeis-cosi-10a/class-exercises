# Plagiarism detector

Write a (very poor) plagiarism detector which compares two student's submissions, and prints some similarity metrics for them:
* The number of unique words which are used across both submissions
* The number of unique words used in one submission, but not the other
* A "plagiarism score" for each student: `# of unique words used in both submissions / # of words unique to student's submission`

Your plagiarism detector should be a function in [code.py](code.py): `compare(submission1, submission2)`, where both submissions are are strings.
