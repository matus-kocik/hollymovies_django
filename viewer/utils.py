from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Avg, Min, Max



class DisplayTitle:
    def display_title(self) -> str:
        if self.title_sk:
            return f"{self.title_sk} ({self.year})"
        elif self.title_cz:
            return f"{self.title_cz} ({self.year})"
        else:
            return f"{self.title_orig} ({self.year})"


class Utils:
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

    @classmethod
    def calculate_age(cls, birth_date, death_date=None):
        if birth_date:
            if death_date:
                delta = relativedelta(death_date, birth_date)
                return delta.years
            else:
                today = date.today()
                delta = relativedelta(today, birth_date)
                return delta.years
        return None
    

class RatingMethods:
    @classmethod
    def calculate_average_rating(cls, queryset):
        average_rating = queryset.aggregate(Avg('rating'))['rating__avg']
        return round(average_rating) if average_rating is not None else None

    @classmethod
    def calculate_min_rating(cls, queryset):
        return queryset.aggregate(Min('rating'))['rating__min']

    @classmethod
    def calculate_max_rating(cls, queryset):
        return queryset.aggregate(Max('rating'))['rating__max']

    @classmethod
    def display_average_rating(cls, movie):
        average_rating = cls.calculate_average_rating(movie.rating_set)
        return f"Average rating: {average_rating}" if average_rating is not None else "Rating not available."

    @classmethod
    def display_min_rating(cls, movie):
        min_rating = cls.calculate_min_rating(movie.rating_set)
        return f"Minimal rating: {min_rating}" if min_rating is not None else "Rating not available."

    @classmethod
    def display_max_rating(cls, movie):
        max_rating = cls.calculate_max_rating(movie.rating_set)
        return f"Maximal rating: {max_rating}" if max_rating is not None else "Rating not available."