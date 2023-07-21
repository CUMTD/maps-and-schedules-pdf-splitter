## NOTE: always manually check the PDFs before you upload them! this script is a bit hacky since it searches the PDFs by headers.

# what it do?
This script takes a PDF of a maps and schedules book and splits it up into a bunch of smaller PDFs for each route [(example for Yellow -- see the "Download" button.)](https://mtd.org/maps-and-schedules/routes/1-yellow-weekday-day/)

# requirements
* Python
* pip package manager
* [pypdf](https://pypdf.readthedocs.io/en/stable/) (install with `python -m pip install pypdf`)

# usage
`python ./script.py [relative path of .pdf]` 

Output PDFs can be found in `output/`.