projecteGDSA
============

Image classification social event in 2013:

1_datasets

Recorded images with specific data type objects Dataset
Train and Test folder creation directori.txt

2_vocabulary

From the train images, creating the two vocabularies type TextVocabulari the textual descriptor from the TF-IDF, and the visual from the SIFT.

3_bof

Creating vector type BofExtractor from vocabulary and file dataset created in section 1

4_tfidf

Creation of vector text descriptors TfidfExtractor

5_annotation

Creating object ontology.p where you store the semantic tags, and where anotation.p added information that belongs to the class of each image and label semantics and deserves.

6_models

Creating the model trainer from objects anotation, train classifier

7_Detector

Classification of images from the model. Creating the object detector, returns an object of type anotation the class name semantics assigned

8_evaluation

Checking labeled. Ground truth for each event, precision, recall and F1-Score



















