# @c Copyright (C) 2014 
# @c Free Software Foundation, Inc.
# @c See the file README for copying conditions. 

import os

from modules.computation.Dataset import Dataset

def _main():
    print "HOla"
    pathHome = os.path.expanduser('~')
    #pathHome=os.path.abspath('/home/alex/Documentos/GDSAProjecte/Pyxel/emohe-pyxel-deb01cc5202e')

    
    pathWork = os.path.join( pathHome,'Documentos','GDSAProjecte')
    #pathWork = os.path.join(pathHome, 'tools','socialevent','mediaeval2013','classification' )
    pathImages = os.path.join(pathWork, '1_images')
    pathDatasets = os.path.join( pathWork, '2_datasets' )
    
    # For each data partition (train & test)
    for partition in os.listdir(pathImages):
        
        # If it is a directory 
        dirPartition = os.path.join( pathImages, partition )
        if os.path.isdir(dirPartition):
        
            # Define the filename to contain the list of images to process
            filenameOut = os.path.join( pathDatasets, partition + '.txt')
            
            dataset = Dataset( filenameOut, 
                            flagSaveInMemory=False, 
                            flagVerbose=True)
    
            dataset.build( dirPartition, '.jpg' )

#def run():
_main()
