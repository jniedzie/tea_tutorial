nEvents = -1
printEveryNevents = 1000
inputFilePath = "../samples/background_dy.root"
histogramsOutputFilePath = "../samples/histograms/background_dy.root"

weightsBranchName = "genWeight"

extraEventCollections = {
    "GoodLeptons": {
        "inputCollections": ("Muon", "Electron"),
        "phi": (0., 2.),
    },
}

defaultHistParams = (
#  collection      variable          bins    xmin     xmax     dir
  ("GoodLeptons" , "pt"            , 400,    0,       200,     ""  ),
  ("GoodLeptons" , "eta"           , 100,    -2.5,    2.5,     ""  ),
)