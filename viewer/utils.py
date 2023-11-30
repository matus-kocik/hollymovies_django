class DisplayTitle:
    def display_title(self) -> str:
        if self.title_sk:
            return f"{self.title_sk} ({self.year})"
        elif self.title_cz:
            return f"{self.title_cz} ({self.year})"
        else:
            return f"{self.title_orig} ({self.year})"
        
class Ordering:
    @classmethod
    def get_ordering(cls, class_name):
        if class_name == "Country" or class_name == "Genre":
            return ["name"]
        elif class_name == "Person":
            return ["last_name", "first_name"]
        elif class_name == "Movie":
            return ["title_sk", "title_cz", "title_orig"]
        elif class_name == "Rating" or class_name == "Comment":
            return ["-created"]
        elif class_name == "Image":
            return ["movie__title_sk", "movie__title_cz", "movie__title_orig"]
        else:
            return []