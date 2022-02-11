from PIL import Image, ImageDraw, ImageFont
import random
import urllib.request, json
import config

#start by getting info about the book

# a few isbns tp play with:
#   0441172717 - Dune
#   1503253791 - Candide
#   0553293354 - Foundation
#   1636768431 - Getting out of Control

isbns = ["0441172717", "1503253791", "0553293354", "1636768431"]
isbn = random.choice(isbns)
APIkey = config.APIkey
searchURL = "https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}".format(isbn, APIkey)
with urllib.request.urlopen(searchURL) as url:
    data = json.loads(url.read().decode())

#assemble facts about the book
BookSpineColors = ["Red", "Green", "Brown", "Blue"]
WhichBook = random.choice(BookSpineColors)
WhichAuthor = data["items"][0]["volumeInfo"]["authors"][0]
WhichTitle = data["items"][0]["volumeInfo"]["title"]

Author_xy = (0,0)
Title_xy = (0,0)

match WhichBook:
    case "Red":
        Title_xy = (450,35)
        Author_xy = (72,770)
    case "Blue":
        Title_xy = (401,72)
        Author_xy = (71,650)
    case "Brown":
        Title_xy = (353,72)
        Author_xy = (72,670)
    case "Green":
        Title_xy = (495,103)
        Author_xy = (103,650)

#Read image
origImage = Image.open(f'BookSpines\{WhichBook}Book.png')
outputImage = ImageDraw.Draw(origImage)

AuthorFont = ImageFont.truetype("Yagora.ttf", 20)
outputImage.text(Author_xy, WhichAuthor, fill="white", anchor="mm", font=AuthorFont)

TitleFont = ImageFont.truetype("Yagora.ttf", 40)
rotatedImage = origImage.transpose(method=Image.ROTATE_270)

nowRotated = ImageDraw.Draw(rotatedImage)
nowRotated.text(Title_xy, WhichTitle, fill="white", anchor="mm", font=TitleFont)

DisplayBook = rotatedImage.transpose(method=Image.ROTATE_90)

#Display image
DisplayBook.show()
