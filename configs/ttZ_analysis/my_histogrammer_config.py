nEvents = -1
printEveryNevents = 1000
inputFilePath = "../samples/background_dy.root"
histogramsOutputFilePath = "../samples/histograms/background_dy.root"
defaultHistParams = (
# collection variable bins xmin xmax dir
("Electron", "pt" , 400, 0 , 200,
"" ),
("Electron", "eta" , 100, -2.5 , 2.5,
"" ),
)
weightsBranchName = "genWeight"