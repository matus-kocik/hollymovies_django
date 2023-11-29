# Movies database

## Database
- Country
  - Name
- Genre
  - Name
- Movies
  - Original title movie
  - CZ title movie
  - SK title movie
  - Country -> FK(Countries)
  - Genre -> FK(Genre)
  - Directors -> FK(Person)
  - Actors -> seznam FK(Person)
  - Year
  - Rating -> FK(Rating)
  - Comment -> FK(Comment)
  - Image -> FK(Image)
  - video -> url odkaz na youtube na trailer
  - description
- Ratings
  - id movie
  - id user
  - rating (rate 0-100 in %)
- Comments
  - id movie
  - id user
  - comment
- Images
  - id movie
  - image (file name/image ?)
  - description
- Person
  - Firstname
  - Lastname
  - Birthdate
  - Biography

TODO: Change later (translate):

## Funkce (views + templates)
- zobrazit novinky (homepage)
- zobrazit seznam všech filmů
- filtrování filmů (seznam) 
  - podle žánru
  - podle hodnocení
  - podle herce
  - podle režiséra
- zobrazit detail filmu
- přihlášený uživatel může:
  - hodnotit filmy
  - komentovat filmy
- admin může:
  - přidat/editovat/smazat film/herce/režiséra/žánr/země/komentáře