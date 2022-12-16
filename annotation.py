class annotation:
    def __init__(self, bookID, booktitle, author, color, createdtime, modifiedtime, paragraph, note, locationrangestart, content):
        self.bookID = str(bookID)
        self.booktitle = str(booktitle)
        self.author = str(author)
        self.color = str(color)
        self.createdtime = str(createdtime)
        self.modifiedtime = str(modifiedtime)
        self.paragraph = str(paragraph)
        self.note = str(note)
        self.locationrangestart =str(locationrangestart)
        self.content = str(content)

    def __str__(self):
        return self.bookID + ", " + self.booktitle + ", " + self.author + ", " + self.color + ", " + self.createdtime + ", " + self.modifiedtime + ", " + self.paragraph + ", " + self.note + ", " + self.locationrangestart + " " + self.content

    def getContent(self):
        return self.content

    def getNote(self):
        return self.note

    def getColor(self):
        return self.color

    def getParagraph(self):
        return self.paragraph

    def getBookID(self):
        return self.bookID

    def getBookTitle(self):
        return self.booktitle

    def getAuthor(self):
        return self.author

    def getCreatedTime(self):
        return self.createdtime

    def getModifiedTime(self):
        return self.modifiedtime

    def getLocationRangeStart(self):
        return self.locationrangestart