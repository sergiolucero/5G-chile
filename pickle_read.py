import pickle, glob

textos = {fn: pickle.load(open(fn,'rb')) for fn in glob.glob('G*.pk')}

print(textos['GS3UA2KO.pk'][:30])
