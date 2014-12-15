# @c Copyright (C) 2014 
# @c Free Software Foundation, Inc.
# @c See the file README for copying conditions. 


# tool to classify new images by using models created 

import os
import time
import pickle
from modules.classification.Detector import Detector
from modules.classification.Ontology import Ontology


def main():
#if __name__ == "__main__":
    print " Funcio principal executant-se..."
    pathHome = os.path.expanduser('~')
    pathWork = os.path.join( pathHome, 'Documentos','GDSAProjecte' )    
    # load models from path:
    pathDirModels = os.path.join( pathWork, '5_models')
    # load fueatures from path:
    pathDirDatasets = os.path.join( pathWork,'2_datasets')
#    pathDirFeaturesImage = os.path.join(pathWork,'4_bof','test')
    pathDirFeaturesText = os.path.join(pathWork,'4_tfidf','test')
    
#    pathFileVisualModel = os.path.join(pathDirModels,'visual_model_svm.p')
    pathFileTextualModel = os.path.join(pathDirModels,'textual_model_svm_annotation.p')
    
    # Ontology
    ontologyFile = 'ontology.p'
    ontologyPathFile = os.path.join(pathDirDatasets, ontologyFile)
    
    ontology = pickle.load(open(ontologyPathFile, 'rb'))
    
    
    # Init detectors
    #visual_detector = Detector(pathFileVisualModel, ontology )
    textual_detector = Detector(pathFileTextualModel, ontology)
    
    # file with test images ids
    pathFileDataset = os.path.join( pathDirDatasets, 'test.txt')
    
    # Run detectors
#    t_ref = time.time()
#    print 'Detecting visual test images...'
    
#    visual_detector.predict_collection( pathFileDataset, pathDirFeaturesImage )
    
#    visual_time = time.time() - t_ref
#    print 'Visual classifier detected in ' , visual_time, ' seconds'

    print 'Detecting textual text images...'
    t_ref = time.time()
    textual_detector.predict_collection( pathFileDataset,pathDirFeaturesText )
    
    textual_time = time.time() - t_ref
    print 'Textual classifier detected in ',textual_time, ' seconds'
    
    #path to save results
    pathDirResults = os.path.join( pathWork,'6_results')
    #file to save results
#    pathFileVisualResults = os.path.join( pathDirResults,'visual_results.txt')
    pathFileTextualResults = os.path.join( pathDirResults,'textual_results_g13.txt')
        
    # Save resuts to file
#    visual_detector.save_to_file(pathFileVisualResults)
    textual_detector.save_to_file(pathFileTextualResults)
    
    
#def run():
main()
    
