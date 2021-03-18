import json
import requests

from typing import Dict
from functools import partial
from bs4 import Tag, BeautifulSoup
from schema import Or, Use, Schema

# url:  URL of the glitches database.
# H:    The header length.
# F:    The footer length.
url = "http://www.jb.man.ac.uk/pulsar/glitches/gTable.html"
H = 5
F = 16


def references(tag: Tag):

    """
    Parse the references as (name, link) pairs into a dictionary.
    """

    return {
        "REFS": {
            str(i + 1): atag["href"]
            for (
                i,
                atag,
            ) in enumerate(tag("a"))
        }
    }


# A simple function to deal with numeric values that could possibly be NULL.
isnull = lambda x, A: A * float(x) if x != "X" else None

# The key-value map for the database.
kvs = {
    "NAME": Use(str),
    "JNAME": Use(str),
    "COUNT": Use(int),
    "MJD": Use(partial(isnull, A=1.0)),
    "MJD_ERR": Use(partial(isnull, A=1.0)),
    "DF/F": Use(partial(isnull, A=1e-9)),
    "DF/F_ERR": Use(partial(isnull, A=1e-9)),
    "DF1/F1": Use(partial(isnull, A=1e-3)),
    "DF1/F1_ERR": Use(partial(isnull, A=1e-3)),
    "REFS": Or({}, {str: str}),
}


def scrap() -> None:

    """
    Scrap the glitches database and serialise it into a JSON file.
    """

    glitches: Dict = {}

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.table("tr")[H:-F]

    for i, row in enumerate(rows):
        refs = row("td")[-1]
        values = [item.text.strip() for item in row("td")[1:-1]]
        glitch = {key: value for key, value in zip(kvs.keys(), values)}
        glitch.update(references(refs))
        glitches[str(i + 1)] = Schema(kvs).validate(glitch)

    with open("glitches.json", "w+") as fobj:
        json.dump(
            glitches,
            fobj,
            indent=4,
        )


if __name__ == "__main__":

    scrap()