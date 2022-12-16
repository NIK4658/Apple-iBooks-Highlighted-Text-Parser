from pickletools import long1
import sqlite3
import books
import annotation
import datetime
import re

# Apple Epoch Start
APPLE_EPOCH_START = int((datetime.datetime(2001, 1, 1)-datetime.datetime.utcfromtimestamp(0)).total_seconds()*1000)

def main():
  # CONSTANTS
  TITLE = "ZTITLE"
  AUTHOR = "ZAUTHOR"
  BOOKID = "ZASSETID"

  COLOR = "ZANNOTATIONSTYLE"
  CONTENT = "ZANNOTATIONSELECTEDTEXT"
  PARAGRAPH = "ZFUTUREPROOFING5"
  NOTE = "ZANNOTATIONNOTE"
  CREATEDTIME = "ZANNOTATIONCREATIONDATE"
  MODIFIEDTIME = "ZANNOTATIONMODIFICATIONDATE"
  LOCATIONRANGESTART = "ZPLLOCATIONRANGESTART"

  BOOKSTABLE = "ZBKLIBRARYASSET"
  ANNOTATIONSTABLE = "ZAEANNOTATION"

  # VARIABLES
  array_books = []
  array_annotations = []
  i=0

  # TEXT ANNOTATION AND BOOKS DATABASES
  conn_Text = sqlite3.connect('Database/Annotations.sqlite')
  cursor_Text = conn_Text.cursor()
  conn_books = sqlite3.connect('Database/books.sqlite')
  cursor_books = conn_books.cursor()

  # Get all books
  cursor_books.execute("select "+BOOKID+" as ID, "+TITLE+" as TITLE, "+AUTHOR+" as AUTHOR from "+BOOKSTABLE+" order by "+BOOKID)

  # Insert all books into an array
  recordsNotes = cursor_books.fetchall()

  for row in recordsNotes:
      array_books.append(books.book(row[0], row[1], row[2]))

      # Get all annotations of that book
      cursor_Text.execute("SELECT "+COLOR+", "+CREATEDTIME+", "+MODIFIEDTIME+", "+PARAGRAPH+", "+NOTE+", "+LOCATIONRANGESTART+", "+CONTENT+" FROM "+ANNOTATIONSTABLE+" WHERE ZANNOTATIONDELETED = 0 AND "+CONTENT+" != 'NULL' AND ZANNOTATIONASSETID = '" + row[0] + "' order by ZANNOTATIONASSETID, "+LOCATIONRANGESTART )

      # Insert all annotations into an array
      recordsNotes = cursor_Text.fetchall()

      # Avoid special characters in file name
      Title = re.sub('[^A-Za-z0-9]+', '', row[1])

      with open('Output/' + Title + '.txt', 'w', encoding="utf-8") as f:
        print("------------------------")
        print("Writing file: " + Title + ".txt")
        for annotationRow in recordsNotes:
          # Check if chapter is null
          if(annotationRow[3]==None):
            chapter = "NULL"
          else:
            chapter = annotationRow[3].rstrip()

          # Insert annotation into array
          array_annotations.append(annotation.annotation(row[0], row[1], row[2], annotationRow[0], convertAppleTime(annotationRow[1]), convertAppleTime(annotationRow[2]), chapter, annotationRow[4], annotationRow[5], annotationRow[6].rstrip()))

          # Check if personal note is not null
          # Check if annotation is header1
          if(array_annotations[i].getNote()==".h1"):
            f.write(str("\n"+"# "+ array_annotations[i].getContent() + "\n"))

          # Check if annotation is header2
          elif(array_annotations[i].getNote()==".h2"):
            f.write(str("\n"+"## "+ array_annotations[i].getContent() + "\n"))

          # Check if annotation is header3
          elif(array_annotations[i].getNote()==".h3"):
            f.write(str("\n"+"### "+ array_annotations[i].getContent() + "\n"))

          # Insert annotation into file
          elif(array_annotations[i].getContent() != ""):
            f.write(str("- " + array_annotations[i].getContent()))
            # Add color indication to annotation
            match array_annotations[i].getColor():
              # case "Underline":
              case "0":
                f.write(" COLOR: UNDERLINE" + "\n")

              # case "Green":
              case "1":
                f.write(" COLOR: GREEN" + "\n")

              # case "Blue":
              case "2":
                f.write(" COLOR: BLUE" + "\n")

              # case "Yellow":
              case "3":
                f.write(" " + "\n")

              # case "Red":
              case "4":
                f.write(" **COLOR: RED**" + "\n")

              # case "Purple":
              case "5":
                f.write(" COLOR: PURPLE" + "\n")
          i+=1
      f.close()
      print("File " + Title + ".txt created")

# Convert Apple Time
def convertAppleTime(appleTime):
  return int(int(APPLE_EPOCH_START + (appleTime * 1000))/1000);

# Main function
if __name__ == "__main__":
  main();
  print("------------------------")
  print("Operation completed");