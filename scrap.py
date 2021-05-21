from json import dump
from requests import get
from bs4 import BeautifulSoup
from typing import Dict, Union, Optional

data: Dict[
    str,
    Dict[
        str,
        Optional[
            Union[
                str,
                int,
                Dict,
                float,
            ]
        ],
    ],
] = {}


rows = BeautifulSoup(
    markup=get("http://www.jb.man.ac.uk/pulsar/glitches/gTable.html").content,
    features="lxml",
).table("tr")[5:-16]


for i, row in enumerate(rows):
    cells = [_.text.strip() for _ in row("td")[1:-1]]
    glitch = {
        key: (None if cell == "X" else factor * conv(cell))
        for (key, conv, factor), cell in zip(
            [
                ("NAME", str, 1),
                ("JNAME", str, 1),
                ("Glitch number", int, 1),
                ("MJD", float, 1),
                ("MJD_ERR", float, 1),
                ("DeltaF/F", float, 1e-9),
                ("DeltaF/F_ERR", float, 1e-9),
                ("DeltaF1/F1", float, 1e-3),
                ("DeltaF1/F1_ERR", float, 1e-3),
            ],
            cells,
        )
    }
    glitch["References"] = {
        str(k + 1): _["href"] for k, _ in enumerate(row("td")[-1]("a"))
    }
    data[str(i + 1)] = glitch


with open("glitches.json", "w+") as fobj:
    dump(
        obj=dict(data=data),
        fp=fobj,
        indent=4,
    )
