#Relevant metadata:
#Namn, dokumenttyp, process (3.4 medlemstöd), organisation (vem TAM har gjort dealen med), Klassificering (Publikt, internt), 
#Personuppgifter (inga, finns, känsliga), dokumentdatum, person som gav ut.

import torch
from transformers import pipeline

qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")

#"Vad är detta för dokument?" "Vad är detta för process?" "Vilket företag gäller dokumentet?" "Vad är dokumentdatumet?" "Vem är referensperson?" 

questionDocument = "Vad är referensen?"

context = """
Sida: 1
Referens: Lars-Erik Hansen
Direkttel: 08-54 54 15 61
lars-erik.hansen@tam-arkiv.se

Protokoll


Sammanträde: Ordinarie stämma

Tid:                   Måndagen den 25 maj 2009 kl.9.30-14.00

Plats:                 TAM-Arkiv, Grindstuvägen 48-50, Bromma

Ombud:            Enligt bil. A


§ 1   Stämmans öppnande		
Ombud och övriga närvarande hälsades välkomna av TAM-Arkivs ordförande Solweig Eklund, som därefter förklarade stämman öppnad.

§ 2   Upprop av ombud
Förrättades upprop av ombuden (bil. A). 

§ 3  Stämmans behörighet
Förklarades stämman behörigen utlyst

§ 4   Val av stämmofunktionärer
Valdes till ordförande Sonja Åström (LR), till sekreterare Lars-Erik Hansen (TAM-Arkiv) och till justerare, tillika rösträknare, Johanna Tüll (Polisförbundet) och Mikael Wikström (Civilekonomerna).

§ 5  Dagordning
Den föreslagna dagordningen fastställdes.

§ 6   Styrelsens verksamhetsberättelser för åren 2006-2008 (bil. 1a – 1c)
Lades med godkännande till handlingarna.

§ 7   Revisionsberättelser för åren 2006-2008 (bil. 2a – 2c)
Lades med godkännande till handlingarna.

§ 8   Resultat- och balansräkningar för åren 2006 - 2008  (bil. 1a – 1c) 
Fastställdes resultat- och balansräkningar för åren 2006 – 2008.
	
§ 9   Disposition av överskott/underskott åren 2006 – 2008 (bil. 1a – 1c)
Överfördes för respektive år i ny räkning.

§ 10  Ansvarsfrihet
Beviljades styrelsen ansvarsfrihet för 2006-2008 års förvaltning.
"""

res = qa_model(question = questionDocument, context = context)

answer_DocumentType = res['answer']

print(res)
#print(answer_DocumentType)


"""FÖRHANDLINGSUNDERLAG 2007

Namn			
	
Nuvarande lön	
	
	


INSATSER UNDER ÅRET

Vad vill du ta upp som viktiga argument över vad du gjort under året och som du är stolt över? t.ex. utförda prestationer eller uppnådda mål såsom genomfört konferenser, projekt, rapporter, drivit igenom en viktig fråga, har god samarbetsförmåga,  skapat ett nytt arbetsområde



Har du fått ökat ansvar under året? t.ex. utökat sakansvar 



Har du tagit initiativ som utvecklat dig och ditt arbete? t.ex. förbättrat arbetsrutiner eller den sociala miljön, initierat samarbete med våra medlemmar eller andra organisationert 



Har du utvecklat din kompetens under året? På vilket sätt? t.ex. lärande i arbetet, läst extra på kvällarna, studerat på universitetet



På vilket sätt anser du att din kompetens är värdefull för TAM-Arkiv?




Anser du dig missgynnad ur lönesynpunkt? På vilket sätt? t.ex. lägre lön än andra med samma utbildning och arbetsuppgifter



Känner du till hur din lön, i din yrkesgrupp, ligger till i förhållande till andra myndigheter eller företag? Hur ligger du i såfall till? De flesta fackförbund tillhandahåller lönestatistik för sina medlemmar, se  t.ex. DIKs lönestatistik på www.dik.se 






"""