# Apple-iBooks-Highlighted-Text-Parser 📝 ![StatusBadge](https://badgen.net/badge/Status/Completed/green) 

### This Python script exports all **notes** from the *iBooks database* and creates a *txt file* for each book.

The script **also handles the annotation colors, they will be annotated apart from the actual annotation**.

It's possible to *annotate a single annotation* in three different ways **in order to let the script interpret that annotation as a chapter title**.

You can use:
- *".h1" to mark as **HEADING 1** (Larger)*
- *".h2" to mark as **HEADING 2** (Medium)*
- *".h3" to mark as **HEADING 3** (Smallest)*

___

## **FEATURES:**
- Automatically extract every single important information of every note and book from iBooks Databases.
- Automatic formatting of the content of each note to ensure full compatibility with the txt file.
- Creation of individual txt files containing the annotations of each book.
- Inserting annotation colors.
- Inserting chapter titles.
- Split txt file with chapter titles.

---

## **USAGE:**
 1. Download the latest release of *Python*.
 2. Download the latest release of the project. 
 3. Insert a copy of the two iBooks Databases in the "Database" folder. (You can use my [Apple-iBooks-Database-Exporter](https://github.com/NIK4658/Apple-iBooks-Database-Exporter) project to export the two databases). 
 4. **Run TextParser.py**.
 5. ALL the txt files will be created in the "Output" folder.

---

## **COMPATIBILITY:**

This script **can be run on any operating system**.

Databases **must first be exported** from a *Mac computer*.

---

## **CHECK ALSO:**

### [Apple-iBooks-Database-Exporter](https://github.com/NIK4658/Apple-iBooks-Database-Exporter):
Automatic script that **locate and generate a copy** of the two iBooks Databases.

### [Apple-iBooks-Highlighted-Text-Exporter](https://github.com/NIK4658/Apple-iBooks-Highlighted-Text-Exporter):
This Python script exports all notes, books and authors from the iBooks database **to a private database**.

---
