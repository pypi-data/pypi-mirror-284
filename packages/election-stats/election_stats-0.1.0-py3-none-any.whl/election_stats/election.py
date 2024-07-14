import pandas as pd


class Candidate:
    def __init__(self, info) -> None:
        self.party = info["party"]
        self.name = info["name"]
        self.votes = info["votes"]
        self.share = info["share"]


class Party:
    PARTY_COLOURS = {
        "Con": "#0087DC",
        "Lab": "#E4003B",
        "LD": "#FAA61A",
        "SNP": "#FDF38E",
        "DUP": "#D46A4C",
        "Green": "#02A95B",
        "SF": "#326760",
        "SDLP": "#2AA82C",
        "Ref": "#12B6CF",
        "PC": "#005B54",
        "APNI": "#F6CB2F",
        "Spk": "black"
    }
    def __init__(self, name) -> None:
        self.name = name[0]
        self.abbrv = name[1]
        self.seats = 0
        self.seat_list = []
        self.colour = Party.PARTY_COLOURS.get(self.abbrv, "grey")


class Parties(dict):
    def get(self, key: tuple[str, str] | str) -> Party:
        if key[0] == "Labour and Co-operative":
           key = ("Labour", key[1])
        if isinstance(key, tuple):
            if not key in self:
                self[key] = Party(key)
            return self[key]
        # if key in [x[0] for x in self.keys()] + [x[1] for x in self.keys()]:
        for k, v in self.items():
            if key in k:
                return v
        raise ValueError("Parties.get argument must be a tuple")


class Constituency:
    def __init__(self, election, name) -> None:
        self.name = name
        self.candidates = []
        self.election = election

    def add_data(self, row) -> None:
        self.candidates.append(Candidate({
            "party": self.election.parties.get((row["Party name"], row["Party abbreviation"])),
            "name": row["Candidate first name"] + " " + row["Candidate surname"],
            "votes": int(row["Votes"]),
            "share": float(row["Share"])
        }))
        self.candidates.sort(key=lambda d: d.votes, reverse=True)
        self.winner = self.candidates[0]


class Election:
    def __init__(self, filename) -> None:
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError as e:
            raise ValueError(e.args) # value is so that argparse catches it without me having to do fancy stuff : https://docs.python.org/3/library/argparse.html#type
        self.constituencies = {}
        self.parties = Parties()
        for index, row in df.iterrows():
            name = row["Constituency name"]
            if not name in self.constituencies.keys():
                self.constituencies[name] = Constituency(self, name)
            self.constituencies[name].add_data(row)

        for c in self.constituencies.values():
            c.winner.party.seat_list.append(c)
            c.winner.party.seats += 1
        self.parties = Parties(
            sorted(self.parties.items(), key=lambda i: i[1].seats, reverse=True))
        self.winner = self
