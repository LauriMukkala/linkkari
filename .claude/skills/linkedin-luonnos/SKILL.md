---
name: linkedin-luonnos
description: Luo uusi LinkedIn-luonnos postaukset/-kansioon. Käytä kun käyttäjä pyytää uutta postausta, luonnosta tai sisältöideaa tekstiksi.
---

# Ennen kirjoittamista

1. Lue `ohjeet/uusi-postaus.md`, `saannot.md` ja `aani.md`.
2. Lue kolme viimeisintä tiedostoa `postaukset/`-kansiosta (nimi
   laskevassa järjestyksessä).
3. Varmista että sinulla on aihe ja julkaisupäivä (DDMM). Jos puuttuu,
   kysy ennen kuin kirjoitat.

# Kirjoita

- Luo **yksi** tiedosto: `postaukset/DDMM-aihe.md` (pienet kirjaimet,
  väliviiva sanojen välissä).
- Noudata `aani.md`: yksi ajatus per rivi, tyhjä rivi kappaleiden välissä.
- Noudata `saannot.md`: kielletyt sanat, korvaukset ja rajat.
- Älä keksi lukuja, asiakastarinoita tai lupauksia. Käytä vain käyttäjän
  antamia faktoja.
- Älä kirjoita `out/`-kansioon.

# Tarkista heti

Aja:

```sh
python3 tarkistus.py postaukset/DDMM-aihe.md
```

# Palauta tässä järjestyksessä

1. TIEDOSTO    polku luotuun tiedostoon
2. LUONNOS     postauksen teksti sellaisenaan
3. LINTTERI    tarkistus.py:n tuloste (tai "0 huomiota")
4. RAJAT       oma tarkistus: näkyvyysraja 210, hashtagit, CTA, linkit
5. TOISTO      sanat tai kulmat, jotka toistuvat viimeisistä postauksista
6. SEURAAVA    yksi ehdotus mitä ihminen voisi vielä tarkistaa

# Rajat

- Älä kirjoita useampaa vaihtoehtoa ellei käyttäjä pyydä.
- Älä muokkaa olemassa olevia postauksia.
- Älä julkaise mitään.
