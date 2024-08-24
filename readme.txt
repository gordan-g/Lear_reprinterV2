Requirements:

1.File programa("ReprinterV2") mora da se nalazi na lokaciji "C:\Users\ggrozdanic\Python" umesto "ggrozdanic" unesite naziv vaseg usera!

2. Program radi samo za Volvo familije(BEV, ICE, SPA)

3. Stampac je u kodu namesten na "LPT2"(serijski) port, stoga je potrebno prilagoditi kod portu na kom se vas stampac nalazi.

4. Ukoliko je stampac sa racunarom povezan preko "USB" porta, pre njegove upotrebe potrebno je odraditi odredjenu konfiguraciju posto inace nije moguce stampati preko cmd.
Prvo je potrebno share-ovati stampac i dodeliti mu ime, zatim se otvori cmd i kuca sledeca komadna 
"net use lpt1(ili neki drugi lpt port): \\nazivracunara\nazivpodeljenogstampaca /persistent:yes" nakon ovih koraka probati odstampati jednu nalepnicu preko cmd i ukoliko stampa
bez problema stampac je dobro konfigurisan.


Errors:

1. Ukoliko se skenira aztek kod ili oid sheet iz odgovarajuceg ugla moguce je da prikaze error "Aztec code nije u dobrom formatu!", potrebno je opet skenirati upravno na qr ili aztek code.

2. Ukoliko prilikom stampanja labele dobijemo gresku poput "Polje datuma mora biti popunjena u trazenom formatu!", proveri da li u input polju za datum postoji razmak ili neko slovo, ukoliko postoji
obrisati ga i opet kliknuti na "Print" dugme.

3.Ako se prilikom stapmanja nalepnice dobije barcode koje je siri nego sto bi trebalo da bude, otvoriti zebra setup utilities i poslati preko njega Help.eti
nalepnicu("C:\Users\TS1500-401170-119\Python\ReprinterV2\Calibrate.eti") na stampanje,nakon cega se moze videti da je barcode kako treba da bude.

4.Ako se klikom na "Reprint" dugme dobije gresku poput "Mora biti odradjen print pre reprinta!", znaci da nijedna nalepnica nije odstampana pre klika na "Reprint".