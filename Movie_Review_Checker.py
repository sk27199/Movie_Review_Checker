print("Welcome to the Movie Review Checker")

#List of words for both postive and negative movie reviews
positive_words = ["good","powerful", "compelling","brilliant", "awesome", "fantastic", "insightful", "natural", "a must-see",
                  "a must-watch", "beautiful", "best", "great"]
negative_words = ["bad", "boring", "basic", "dissapointed", "dissapointing", "predictable", "slow", "confusing", "weak", "bored",
                  "headache"]

while True:
    review = input("\n Enter your movie review (or type : exit : to quit): ").lower()

    if review == "exit":
        print("Thank you for using Movie Review Checker! ")
        break

    # counts how many positive and negative words appears
    positive_count = sum(word in review for word in positive_words)
    negative_count = sum(word in review for word in negative_words)

    print(f"\n Positive words found: {positive_count}")
    print(f"Negative words found: {negative_count}")

    if positive_count > negative_count:
        print(" This review seems POSITIVE")
    elif negative_count > positive_count:
        print(" This review seems NEGATIVE")
    else:
        print("This review seems neutral or mixed")