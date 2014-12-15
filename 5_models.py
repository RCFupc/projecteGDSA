# @c Copyright (C) 2014 
# @c Free Software Foundation, Inc.
# @c See the file README for copying conditions. 


# tool to build the textual and visual models

import os
import time
import pickle
from modules.classification.Trainer import Trainer
from modules.classification.Annotation import Annotation
from modules.classification.Ontology import Ontology


if __name__ == "__main__":
    print "hola"
    pathHome = os.path.expanduser('~')
    pathWork = os.path.join( pathHome,'Documentos','GDSAProjecte')    
    pathDirModels = os.path.join( pathWork, '5_models')
    
    # If necessary, create a directory to save the models
    if not os.path.exists(pathDirModels):
        print 'New directory created at ' + pathDirModels
        os.makedirs(pathDirModels)
    
    pathDirDatasets = os.path.join( pathWork,'2_datasets')
    #pathFileFeaturesImage = os.path.join(pathWork,'4_bof','train')
    pathFileFeaturesText = os.path.join(pathWork,'4_tfidf','train')
    ontologyFile = 'ontology.p'
    annotationFile = 'annotation.p'
    annotationSavePathFile = os.path.join(pathDirDatasets, annotationFile)
    ontologyPathFile = os.path.join(pathDirDatasets, ontologyFile)

    # cargar ontology
    ontologyObject = Ontology()
    ontologyObject.loadOntology(ontologyPathFile)

    annotation = Annotation(ontologyObject)
    
    annotation = pickle.load(open(annotationSavePathFile,'rb'))
    #visual_trainer = Trainer(  pathFileFeaturesImage, annotation)
    textual_trainer = Trainer( pathFileFeaturesText, annotation)
    
    # Run trainers
    pathFileDataset = os.path.join( pathDirDatasets, 'train.txt')
    
    #t_ref = time.time()
    #print 'Training with visual features...'
    
    #visual_trainer.run( pathFileDataset )
    
    #visual_time = time.time() - t_ref
    #print 'Visual classifier trained in ' , visual_time, ' seconds'

    print 'Training with textual features...'
    t_ref = time.time()
    textual_trainer.run( pathFileDataset )
    
    textual_time = time.time() - t_ref
    print 'Textual classifier trained in ',textual_time, ' seconds'
    

    # Save models to disk
    textual_trainer.save_model_to_disk( pathDirModels, 'textual_model_svm_annotation.p')
    #visual_trainer.save_model_to_disk( pathDirModels, 'visual_model_svm.p')
    
    
#def run():

print "hola"
