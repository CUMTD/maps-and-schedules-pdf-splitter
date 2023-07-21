from pypdf import PdfReader, PdfWriter
import sys, os

# route names to look for in PDF headers to look for
routes = [
    "Yellow",
    "Red",
    "Lavender",
    "Blue",
    "Green",
    "Orange",
    "Grey",
    "Bronze",
    "Brown",
    "Gold",
    "Ruby",
    "Teal",
    "Silver",
    "Navy",
    "Pink",
    "Lime",
    "Raven",
    "Illini",
    "Link",
    "tranSPORT",
]

# assert first arg is a pdf filepath
filepath = ""
try:
    filepath = sys.argv[1]
    if (filepath[-4:] != ".pdf"):
        raise IndexError
    
except IndexError:
    print("Please provide a filepath to a .pdf file")
    sys.exit(1)

# get the filename without the extension (may need to change \\ to / if not on windows)
original_filename = filepath.split("\\")[-1].strip(".pdf")

print(original_filename)

hits = []

# visitor function that filters out pages that don't have a route name in the header
def visitor_body(text, cm, tm, font_dict, font_size):
    if (
        tm[5] > 700
        and text is not None
        and len(text) > 10
        and type(text) is str
        and any(x in text for x in routes)
        and any(chr.isdigit() for chr in text)
    ):
        if text not in hits:
            hits.append(text)
        return True
    return False

# make a reader and writer object
reader = PdfReader(filepath)
writer = PdfWriter()

# make a new directory 
os.makedirs(f"output/{original_filename}")

# iterate through the pages, writing new pdfs when a new route is found
routes_count = 0
for page in reader.pages:
    if page is not None:
        hits_before = len(hits)

        if page.extract_text(visitor_text=visitor_body):
            if len(hits) > hits_before:
                writer.write(f"./output/{original_filename}/{hits[len(hits) - 2]}.pdf")
                routes_count += 1
                writer = PdfWriter()
                writer.add_page(page)

            else:
                writer.add_page(page)

writer.write(f"./output/{original_filename}/{hits[len(hits) - 1]}.pdf")
routes_count += 1

print(f"all done. {routes_count} routes found.")
