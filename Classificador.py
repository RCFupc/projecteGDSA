import csv
import time
import datetime
import tfidf

timer=time.time()

dades_clas = list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Arxius_Tags\Arxiu_classificador_0679.txt','rb'),delimiter=' '));

doc_id=[];
tags=[];
lon_fi=(len(dades_clas));
m=0;
llista=[];

while(m<lon_fi):
        
    if(m>0):
    
      if(dades_clas[m][0]!=dades_clas[m-1][0]):
           doc_id.append(tags);
           tags=[];
           tags.append(dades_clas[m][1]+'\n');
           llista.append(doc_id);
           doc_id=[];
           doc_id.append(dades_clas[m][0]);
           
      else:
           tags.append(dades_clas[m][1]+'\n');
    
    else:
        doc_id.append(dades_clas[m][0]);
        tags.append((dades_clas[m][1]+'\n'));
        
    m+=1
doc_id.append(tags);    
llista.append(doc_id);

concert = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\concert_ent.txt")
llista_con=concert.readlines()
concert.close()

conference = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\conference_ent.txt")
llista_conf=conference.readlines()
conference.close()

exhibition = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\exhibition_ent.txt")
llista_ex=exhibition.readlines()
exhibition.close()


fashion = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\efashion_ent.txt")
llista_fas=fashion.readlines()
fashion.close()

non_event = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\enon_event_ent.txt")
llista_ne=non_event.readlines()
non_event.close()

other = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\other_ent.txt")
llista_ot=other.readlines()
other.close()

sports = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\sport_ent.txt")
llista_sp=sports.readlines()
sports.close()

theater_dance = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\etheater_dance_ent.txt")
llista_td=theater_dance.readlines()
theater_dance.close()

protest = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Fitxers_sortida_descriptor\protest_ent.txt")
llista_pr=protest.readlines()
protest.close()

tam=len(llista);
itera=0;
cont_id=[];

while(itera<tam):
    cont_concert = 0
    cont_conference = 0
    cont_exhibition = 0
    cont_fashion = 0
    cont_non_event = 0
    cont_other = 0
    cont_sports = 0
    cont_theater_dance = 0
    cont_protest = 0
    maxims=0;
    concert = ['concert']
    conference = ['conference']
    exhibition = ['exhibition']
    fashion = ['fashion']
    other = ['other']
    sports = ['sports']
    theater_dance = ['theater_dance']
    protest = ['protest']
    non_event=['non_event']
    
    table=tfidf.tfidf()
    
    table.addDocument('concert',llista_con)
    table.addDocument('conference',llista_conf)
    table.addDocument('exhibition',llista_ex)
    table.addDocument('fashion',llista_fas)
    table.addDocument('other',llista_ot)
    table.addDocument('sports',llista_sp)
    table.addDocument('theater_dance',llista_td)
    table.addDocument('protest',llista_pr)
    table.addDocument('non_event',llista_ne)
    
    taula = table.similarities(llista[itera][1])

    maxims=(max(taula[0][1],taula[1][1],taula[2][1],taula[3][1],taula[4][1],taula[5][1],taula[6][1],taula[7][1],taula[8][1]))
    
    a=0
    
    while (a<9):
        if(taula[a][1]==maxims):
            cont_id.append([llista[itera][0],taula[a][0]])
            break;
        a=a+1   
                
    itera+=1
    
x=len(cont_id)
i=0
fitxer = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Examen_Final\Resultats_Classificats\classificacio_amb_0679.txt","wb")     
#fitxer.write(str("document_id event_type"+'\n')) #LINIA PER NOSALTRES PER PODER AVALUAR SENSE EDITAR ELS FITXERS A MA
while(i<x):
        fitxer.write(str(cont_id[i][0])+' '+str(cont_id[i][1])) 
        fitxer.write("\n")
        i+=1
   
fitxer.close()

print(str(datetime.timedelta(seconds=(time.time()-timer))))
