# Uusi LinkedIn-postaus

Ohje markkinointitiimille ja Claude Codelle. Lue tämä ennen uuden
luonnoksen kirjoittamista.

## Milloin

Käytä kun tarvitset uuden postauksen aiheesta, jota ei ole vielä
`postaukset/`-kansiossa. Olemassa olevan luonnoksen parantamiseen
käytä skilliä `linkedin-tarkistus`, älä tätä.

## Kerro Claude Codelle

| Tieto | Esimerkki | Pakollinen |
|---|---|---|
| Aihe | dev-työkalut markkinoinnissa | kyllä |
| Julkaisupäivä | 0109 | kyllä (tiedostonimi) |
| Näkökulma | mitä opimme viime viikolla | suositus |
| Luvut ja faktat | 3 päivää vs 9 päivää | vain jos tiedossa |
| Asiakas mainittavaksi | ei / ilman nimeä / nimi + lupa | suositus |

Älä pyydä Claudea keksimään lukuja, asiakastarinoita tai lupauksia.
Jos faktaa ei ole, kirjoita ilman numeroita tai kysy ensin.

## Työjärjestys

1. Claude lukee `saannot.md`, `aani.md` ja kolme viimeisintä tiedostoa
   `postaukset/`-kansiosta.
2. Claude kirjoittaa **yhden** luonnoksen tiedostoon
   `postaukset/DDMM-aihe.md` (pienet kirjaimet, väliviiva).
3. Claude ajaa `python3 tarkistus.py postaukset/DDMM-aihe.md`.
4. Claude raportoi lintterin tulokset ja lyhyen oman tarkistuksen
   (`saannot.md`-rajat: 210 merkkiä, hashtagit, CTA, linkit).
5. Ihminen muokkaa luonnosta. Git diff näyttää muutokset.
6. Hyväksynnän jälkeen valmis teksti kopioidaan `out/`-kansioon.
   Skill `julkaisuvalmius` ajetaan ennen julkaisua.

Claude ei kirjoita suoraan `out/`-kansioon eikä julkaise mitään.

## Tekstin muoto

LinkedIn-postaus kirjoitetaan **yksi ajatus per rivi**. Älä katkaise
lausetta satunnaisesti kesken — jokainen rivi on kokonainen lause tai
lyhyt lausepari.

```
Ensimmäinen rivi on koukku. Se lupaa jotain konkreettista.

Toinen kappale alkaa tyhjällä rivillä.
Yksi lause per rivi.
Kolmas lause samassa kappaleessa.

Neljäs kappale tuo uuden ajatuksen.

Yksi toimintakutsu.

#hashtag1 #hashtag2 #hashtag3
```

## Qalmarin ääni (lyhyt)

- Aloita väitteestä, ei "Olemme innoissamme".
- Konkretia ennen adjektiiveja: mitä tehtiin, kenelle, mikä muuttui.
- Kanta on ok: miksi teemme näin, miksi emme tee toisin.
- IT-konsultti, ei tuote-mainos: Qalmar auttaa asiakasta tekemään,
  ei myy "saumatonta alustaa".
- Yksi CTA postauksessa. Linkki ensimmäiseen kommenttiin, ei leipätekstiin.

Täydellisempi lista: `aani.md`.

## Esimerkkipromptit

```
tee uusi postaus aiheesta dev-työkalut markkinoinnissa, päivä 0109
```

```
kirjoita linkedin-luonnos: asiakkaan löytäminen hakukoneessa,
päivä 1509, ei asiakasnimeä, luvut: aiemmin 2 viikkoa nyt 3 päivää
```

## Tarkistus ennen hyväksyntää

- [ ] Lintteri: 0 VIRHE-riviä
- [ ] Ensimmäinen rivi toimii ilman "Näytä lisää" -klikkausta
- [ ] Ei linkkejä leipätekstissä
- [ ] Enintään 5 hashtagia
- [ ] Enintään 1 toimintakutsu
- [ ] Ei toistoa kolmen viime postauksen sanavalinnoissa
