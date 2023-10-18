nEvents = -1
printEveryNevents = 1000

inputFilePath = "../samples/background_dy.root"
treeOutputFilePath = "../samples/skimmed/background_dy.root"

weightsBranchName = "genWeight"

eventSelections = {
    "nMuon": (1, 9999999),
}