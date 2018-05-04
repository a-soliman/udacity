def read_text():
   quotes = open(r"D:\code\udacity\python\movie_quotes.txt")
   content = quotes.read()
   quotes.close()
   
   return content

read_text()
