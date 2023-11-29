class DisplayTitle:
    def display_title(self) -> str:
        if self.title_sk:
            return f"{self.title_sk} ({self.year})"
        elif self.title_cz:
            return f"{self.title_cz} ({self.year})"
        else:
            return f"{self.title_orig} ({self.year})"