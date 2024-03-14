import os


class Credentials:
    OPEN_AI_KEY = os.environ['OPEN_AI_KEY']
    ELAI_API_KEY = os.environ['ELAI_API_KEY']


class URLs:
    ELAI_API_BASE_URL = 'https://apis.elai.io/api/v1/videos'
