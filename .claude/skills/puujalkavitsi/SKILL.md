---
name: puujalkavitsi
description: Lisää puujalkavitsin olemassa olevaan LinkedIn-luonnokseen. Käytä kun käyttäjä pyytää vitsiä, sanaleikkiä tai kevennystä postaukseen.
---

# Ennen muokkaamista

1. Selvitä, mikä tiedosto `postaukset/`-kansiosta on kyseessä. Jos
   epäselvä, kysy.
2. Tarkista, onko samanniminen teksti jo `out/`-kansiossa (hyväksytty).
   Jos on, älä muokkaa — kerro käyttäjälle, että postaus on jo
   hyväksytty eikä sitä saa muuttaa.
3. Lue `saannot.md` ja `aani.md`.

# Lisää

- Kirjoita **yksi** puujalkavitsi tai sanaleikki omalle rivilleen,
  tyhjillä riveillä ympärillä, CTA:n ja hashtagien väliin.
- Vitsin pitää liittyä postauksen aiheeseen.
- Ei kiellettyjä sanoja (`saannot.md`), ei keksittyjä lukuja tai
  asiakastarinoita.
- Älä muuta koukkua, leipätekstiä, CTA:ta tai hashtageja.

# Tarkista heti

Aja:

```sh
python3 tarkistus.py postaukset/DDMM-aihe.md
```

# Palauta tässä järjestyksessä

1. TIEDOSTO   polku muokattuun tiedostoon
2. VITSI      lisätty rivi sellaisenaan
3. LINTTERI   tarkistus.py:n tuloste (tai "0 huomiota")
4. HUOM       yksi lause: sopiiko vitsi aani.md:n sävyyn vai onko riski

# Rajat

- Älä lisää useampaa kuin yhden vitsin.
- Älä muokkaa jo hyväksyttyä postausta (katso yllä).
- Älä julkaise mitään.
