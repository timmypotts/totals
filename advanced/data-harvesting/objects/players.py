class Player:
    # def __init__(self, team, position, age, bats, throws, atBats, runs, hits, homeRuns, RBIs, Ks, left_on_base, singles, doubles, triples, BA, OBS, OBP, SLG, ID, gameID, ERA):
    #     self.model =
    def __init__(self, ID, name, team, position, age, bats, throws, gamesPlayed):
        self.ID = ID
        self.name = name
        self.team = team
        self.position = position
        self.age = age
        self.bats = bats
        self.throws = throws
        self.gamesPlayed = gamesPlayed

    class Batting:
        def __init__(self, atBats, runs, hits, groundOuts, airOuts, HRs, RBIs, Ks, left_on_base, singles, doubles, triples, BA, BABIP, OBS, OBP, SLG, stolenBases, caughtStealing, ABpHR, gameID):
            self.atBats = atBats
            self.runs = runs
            self.hits = hits
            self.groundOuts = groundOuts
            self.airOuts = airOuts
            self.HRs = HRs
            self.RBIs = RBIs
            self.Ks = Ks
            self.left_on_base = left_on_base
            self.singles = singles
            self.doubles = doubles
            self.triples = triples
            self.BA = BA
            self.BABIP = BABIP
            self.OBS = OBS
            self.OBP = OBP
            self.SLG = SLG
            self.stolenBases = stolenBases
            self.caughtStealing = caughtStealing
            self.ABpHR = ABpHR
            self.gameID = gameID

    class Pitching:
        def __init__(self, IP,  ERA, hits, runs, ERs, BBs, Ks, HRs, singles, doubles, triples, gameID):
            self.ERA = ERA
            self.IP = IP
            self.hits = hits
            self.runs = runs
            self.ERs = ERs
            self.BBs = BBs
            self.Ks = Ks
            self.HRs = HRs
            self.singles = singles
            self.doubles = doubles
            self.triples = triples
            self.gameID = gameID
