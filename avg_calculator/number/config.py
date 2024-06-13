from collections import deque

# Bearer token for API authentication
AUTH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MjYyNTcwLCJpYXQiOjE3MTgyNjIyNzAsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjhhOTM2MmFlLTQzYzktNDM0NS1hNDE0LWQxZWVlZmEyY2NlNiIsInN1YiI6Im1hbmlkZWVwbTc2NkBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJLTCBVTklWRVJTSVRZIiwiY2xpZW50SUQiOiI4YTkzNjJhZS00M2M5LTQzNDUtYTQxNC1kMWVlZWZhMmNjZTYiLCJjbGllbnRTZWNyZXQiOiJPaE1GZE9MaElnbFpxZkF0Iiwib3duZXJOYW1lIjoiTW90aHVrdXJpIE1hbmkgRGVlcCIsIm93bmVyRW1haWwiOiJtYW5pZGVlcG03NjZAZ21haWwuY29tIiwicm9sbE5vIjoiMjEwMDAzMDg5OCJ9.zy161-EQmAG6E-lF5r49QLTycOa8gF8_W-hlpWmCfXo'

# Define the window size for the sliding window
SLIDING_WINDOW_SIZE = 10

# Initialize sliding windows for each number type
sliding_windows = {
    'p': deque(maxlen=SLIDING_WINDOW_SIZE),
    'f': deque(maxlen=SLIDING_WINDOW_SIZE),
    'e': deque(maxlen=SLIDING_WINDOW_SIZE),
    'r': deque(maxlen=SLIDING_WINDOW_SIZE)
}
