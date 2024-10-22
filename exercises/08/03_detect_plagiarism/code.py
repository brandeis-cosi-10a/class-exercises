def compare(submission1, submission2):
    sub1_unique = set(submission1.lower().split())
    sub2_unique = set(submission2.lower().split())

    overlap = sub1_unique.intersection(sub2_unique)
    sub1_only = sub1_unique - sub2_unique
    sub2_only = sub2_unique - sub1_unique

    print(f"Submissions share {len(overlap)} unique words")
    print(f"Submission 1 has {len(sub1_only)} unique words that don't appear in submission 2")
    print(f"Submission 2 has {len(sub2_only)} unique words that don't appear in submission 1")
    if len(sub1_only) > 0:
        print(f"The plagiarism score for submission 1 is: {len(overlap) / len(sub1_only)}")
    else:
        print(f"The plagiarism score for submission 1 is: infinity")
    if len(sub2_only) > 0:
        print(f"The plagiarism score for submission 2 is: {len(overlap) / len(sub2_only)}")
    else:
        print(f"The plagiarism score for submission 2 is: infinity")


compare("The quick brown fox jumps over the red balloon", "quick jumps over a fox are dangerous")
compare("No overlap between these two", "None at all")
compare("These submissions are exactly the same down to the last word", 
        "These submissions are exactly the same down to the last word")