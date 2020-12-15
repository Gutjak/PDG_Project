# PDG_Project
Procedural Dungeon Generator Project

Beskrivelse af problemet:
Programmet laver en tilfældig labyrint med smutveje. I det ene hjørne starter spilleren i det modsatte står en drage.
Man skal igennem labyrinten uden at blive fanget af dragen.

Jeg ville gerne forsøge at lave procedual generated content som kunne vises i et spil.

Bemærk et den anden contributer KrisHolmberg er en af mine venner, der gerne ville prøve min kode. 
Han er tilføjet lidt sprites som kunne bruges, her i blandt dragen. Den eneste kode han har tilføjet er den måde som pygame lukker spillet ned på når man trykker på det røde kryds. Da den måde der står i pygame egen dokumentation ikke rigtig virker, men bare crasher programmet.
Hvis det ser anderledes ud i github, så er det mere et bevis på min manglende erfaring med merging af kode i github.


Beskrivelse af programmet:
Programmet bruger pygame til at understøtte den grafiske struktur og flytte rundt på sprites.
Forskellen mellem om der er mur eller gulv er basseret på om feltet (Tile) er blocked.
Hele brættet er delt op i felter af 32 pixels. Brættet skal være et ulige antal tiles højt og bredt. Apsolut minimum er 5x5 felter. 
Så kan spillet ikke vindes. Det skal over 11x11 før det kan vindes pga. antallet af smutveje. Max er ikke testet.
Først bliver hele brættet dækket af mur. Derefeter bliver der lavet et grid af gulvfelter på alle ulige koordinater. 1,1; 1,3; 1,5; 3,1; 3,3;...

Så bliver labyrinten bygget ved hjælp af en Recursive depth-first search. Den kigger på sine nabo-gulvfelter. Gemmer naboerne i en liste. Listen bliver blandet. Så går den i gang med at gå listen igennem. 
Hvis nabo-gulvfeltet er besøgt (visited) bliver den sprunget over. Hvis den ikke er besøgt bliver muren mellem de to felter fjernet og lavet til gulv. Dette felt er nu det nye udgangspunkt for at finde naboer. 
Ved hjælp af recursive bliver den ved fra det nye felt. Hvis alle naboerne er besøgt vil den gå et step tilbage og prøve den næste nabo i sin liste. Det bliver den ved med indtil alle naboer er besøgt.

For at gøre det mere interessant bliver der smidt smutveje ind. Hvis brættet er meget lille bliver de ikke smidt på da det kan være at der ikke er plads.
Der bliver fundet en tilfældig lige koordinat. 2,2; 2,4; 6,12;... Der tjekkes at det er en mur. Der skal være mur på feltet over og under og frit på højre og venstre eller omvendt. 
Det er for at undgå at der kommer ubrugelige smutveje. Det kunne være enden på en væg eller et hjørne.

Efter splashscreen kan man komme til at spille. Man flytter spilleren ved hjælp af piletaster. Dragen laver en A-star som giver den korteste rute hen til spilleren. Hver gang spilleren flytter sig vil ruten blive opdateret.
Der er ikke taget højde for om spilleren kan nå at komme ud af en blindgyde fra start før dragen fanger ham.

Kommer spilleren i mål (døren) vinder han. Bliver han fanget af dragen taber han. Spillet er dog ikke låst. Så det er muligt at flytte på spilleren selv om man har tabt eller vundet.


Hvis jeg havde mere tid:
	Sørge for at spillet stoppede korrekt og man kunne starte et nyt spil uden at stoppe og starte koden.
	
	Jeg ville lave en sikring på at det er muligt at vinde banen. Lige nu kan man komme ud for at man ikke kan nå at komme af en labyrint del uden at dragen kan nå at dække udgangen af den del.
	Da jeg kender dragens rute, burde det være muligt at se om det er muligt at komme flere veje på de sidste 50% af dragens rute. Det er ruten der vil nå hen til spilleren. 
	Hvis spilleren ikke kan komme til vige fra ruten på de 50% ved jeg at dragen altid vil vinde.

Hvordan kan man lave spillet mere sjovt?
	Tier 1 (realistiske opdateringer)
	Man kunne lægge diamanter rundt omkring som spilleren kan samle op for point og forsøge at lave en highscore. Highscoren skal kunne gemmes.
	Dragen kunne laves dummere, så den ikke opdatere ruten efter hvert flyt. Men måske opdatere hver tredje flyt og nogen vælger at stå stille eller gå baglæns via gammel rute.

	Tier 2 (fullblown feature creep)
	Indfører lukkede døre hvor man skal finde nøgler for at finde ud.
	Andre små monstre der skal besejres på vejen.
	
Konklussion
Det er interessant at se hvor meget en grafisk flade gør for et projekt. Mine tidligere programmer har kun været tekst i konsollen.
Det er mere tydeligt at se hvor langt man er nået