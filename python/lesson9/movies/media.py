import webbrowser
class Movie(object):
    def __init__(self, title, story_line, youtube_trailer, poster_image):
        self.title = title
        self.storyline = story_line
        self.trailer_youtube_url = youtube_trailer
        self.poster_image_url = poster_image
    
    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)

