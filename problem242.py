# Problem Description
# =====================================================================================================================================================================================
# This problem was asked by Twitter.
# You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:
# update(hour: int, value: int): Increment the element at index hour by value.
# query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).
# You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.
# =====================================================================================================================================================================================

NEW_SUBSCRIBERS = [0] * 24

def update(hour, value):
    NEW_SUBSCRIBERS[hour] += value

def query(start, end):
  return sum(NEW_SUBSCRIBERS[start:end+1])

update(1, 5)
update(2, 10)
update(3, 15)

print(query(1, 2))
