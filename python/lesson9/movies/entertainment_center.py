from media import Movie
import fresh_tomatos

toy_story = Movie( "Toy Story", "A story of a boy and his toys that come to life", "https://youtu.be/KYz2wyBy3kc", "https://www.imdb.com/title/tt0435761/mediaviewer/rm3038678784")
avatar = Movie("Avatar", "A marin on an Alian planet", "https://www.youtube.com/watch?v=6ziBFh3V1aM", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jpr")
rampage = Movie("Rampage", "Global icon Dwayne Johnson headlines the action adventure “Rampage,” directed by Brad Peyton. Johnson stars as primatologist", "https://youtu.be/-43MBOJnVks","http://t1.gstatic.com/images?q=tbn:ANd9GcQpTCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ")
avengers_infinity_war = Movie("Avengers: Infinity War", "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy", "https://youtu.be/6ZfuNTqbHE8", "http://t2.gstatic.com/images?q=tbn:ANd9GcQoBtRhueP0Kn_O7e89DXSBKBUz-1Nu4Ngb9eqFzqF3EbPGWYVP")
isle_of_dogs = Movie("Isle of Dogs", "When, by executive decree, all the canine pets of Megasaki City are exiled", "https://youtu.be/twuU-nK7Euw", "http://t0.gstatic.com/images?q=tbn:ANd9GcTlfoV5kQt5-R8rsorM0EIFLABrhl2Fjw8ODib_tHAM3QJUAeB8")
leano_on_pete = Movie("Lean on Pete", "Charley, a teen living with his single father, finds work", "https://youtu.be/xjl0SIAitKQ" , "http://t3.gstatic.com/images?q=tbn:ANd9GcT7cg_UeM7EWnDeqxaGz7qsRGQlpRVnJsQ0OMjKJfqr0gwJMsgz")
sherlock_gnomes = Movie("Sherlock Gnomes", "After a string of garden gnome disappearances in London", "https://youtu.be/sIsFUEDRT70", "http://t0.gstatic.com/images?q=tbn:ANd9GcTRi_2By4YzKHdiLqD-91E2GwQ8V56r7mXN4aIx5ueUuRwNKbcU")

movies = [toy_story, avatar, rampage,avengers_infinity_war, isle_of_dogs, leano_on_pete, sherlock_gnomes]
fresh_tomatos.open_movies_page(movies)