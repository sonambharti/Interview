"""
We have a shop/mart, where we want to find out the oldest first / one-timer user so that we can offer them a best discount.
"""

from collections import defaultdict
from datetime import datetime


from datetime import datetime

def oldest_one_timer_bruteforce(logs):
    oldest_user = None
    oldest_time = None

    for i in range(len(logs)):
        user, timestamp = logs[i]

        count = 0

        # Count occurrences of current user
        for j in range(len(logs)):
            if logs[j][0] == user:
                count += 1

        if count == 1:
            current_time = datetime.strptime(
                timestamp,
                "%Y-%m-%d %H:%M:%S"
            )

            if oldest_time is None or current_time < oldest_time:
                oldest_time = current_time
                oldest_user = user

    return oldest_user
    

def oldest_one_timer(logs):

    count = defaultdict(int)

    for user, _ in logs:
        count[user] += 1

    oldest_user = None
    oldest_time = None

    for user, timestamp in logs:

        if count[user] == 1:

            current_time = datetime.strptime(
                timestamp,
                "%Y-%m-%d %H:%M:%S"
            )

            if oldest_time is None or current_time < oldest_time:
                oldest_time = current_time
                oldest_user = user

    return oldest_user


if __name__ == "__main__":

    logs = [
        ("user1", "2024-01-10 10:00:00"),
        ("user2", "2024-01-15 11:00:00"),
        ("user1", "2024-02-01 09:00:00"),
        ("user3", "2023-12-01 08:00:00"),
        ("user4", "2024-03-10 12:00:00"),
        ("user4", "2024-04-01 14:00:00"),
    ]

    result = oldest_one_timer(logs)

    print("Oldest one-time user:", result)
