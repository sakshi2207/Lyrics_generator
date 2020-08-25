def install(package):
    subprocess.call([sys.executable, "-m","pip","-q", "--disable-pip-version-check", "install", package])
    

install("bs4")
install("requests")

from bs4 import BeautifulSoup as B

import requests

song = (input("Enter your song: ") or "bollywood").lower().strip()
print(song)


def english(art_album, sing):
    ext = ".html"

    url = "https://www.azlyrics.com/lyrics"

    links = "".join([url, "/", artistic, "/", sing_song, ext])

    page = requests.get(links)

    # Parsing the HTML request
    soup = B(page.content, "html.parser")

    # Finding Artist/Album name
    heading = soup.find("div", class_="lyricsh")
    # Extracting Artist/Album name
    heading_extr = heading.get_text()
    print(heading_extr)

    # Finding the lyrics name
    lyrics_name = soup.find_all("b")[1]
    # Extracting the lyrics name
    name_extr = lyrics_name.get_text()
    print(name_extr)

    # Finding the lyrics
    lyrics = soup.find_all("div")[20]
    # Extracting the lyrics
    lyrics_extr = lyrics.get_text()
    print(lyrics_extr)


def hindi(sing):
    ext = ".html"

    url = "https://gaana.com/lyrics/amp/"

    links = "".join([url, sing_song, ext])

    page = requests.get(links)

    # Parsing the HTML request
    soup = B(page.content, "html.parser")

    # Finding the lyrics name
    lyrics_name = soup.find_all("li", class_="current")[0]
    # Extracting the lyrics name
    name_extr = lyrics_name.get_text()
    print(name_extr)
    print()

    # Finding the lyrics
    lyrics = soup.find_all("pre")[0]
    # Extracting the lyrics
    lyrics_extr = lyrics.get_text()
    print(lyrics_extr)


try:
    if song == "hollywood":
        art_album = (
            (input("Enter the (artist/album) name: ") or "celine dion").lower().split()
        )
        artistic = "".join(art_album)
        print(artistic)

        sing = (input("Enter song name: ") or "my heart will go on").lower().split()
        sing_song = "".join(sing)
        print(sing_song)
        print()

        # calling the function
        english(art_album, sing)
    elif song == "bollywood":
        sing = (input("Enter song name: ") or "dil de diya hai").lower().split()
        sing_song = "-".join(sing)
        print(sing_song)
        print()
        
        # calling the function
        hindi(sing)
    else:
        print("Error!!! Read the instructions carefully ")
except:
    print(
        "An Error Occured. Read the instructions carefully and then run the code again"
    )
