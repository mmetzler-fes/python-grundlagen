import * as random from 'random';
var eingabe, erfolg, x, zahl;
x = random.random();
zahl = Number.parseInt(x * 10) + 1;
erfolg = false;

for (var versuche = 1, _pj_a = 6; versuche < _pj_a; versuche += 1) {
  eingabe = input("Rate meine Zahl zwischen 1 und 10: ");
  versuche += 1;

  if (zahl > Number.parseInt(eingabe)) {
    console.log("Meine Zahl ist gr\u00f6\u00dfer");
  } else {
    if (zahl < Number.parseInt(eingabe)) {
      console.log("Meine Zahl ist kleiner");
    } else {
      console.log("Super. Richtig geraten in %d Versuchen" % versuche);
      erfolg = true;
      break;
    }
  }
}

if (!erfolg) {
  console.log("Du hast das Spiel leider verloren");
}
