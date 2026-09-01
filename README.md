# Linkkari

Qalmarin LinkedIn-sisältödemon pohja. Näyttää miten git, CLAUDE.md, skillit
ja yksinkertainen lintteri tukevat postausten kirjoittamista.

Esitys: [git-lint-skillit](../esitykset/git-lint-skillit/index.html)

## Rakenne

| Tiedosto | Tehtävä |
|---|---|
| `CLAUDE.md` | Pysyvät ohjeet Claude Codelle |
| `saannot.md` | Kielletyt sanat, korvaukset ja rajat |
| `aani.md` | Qalmarin sävy LinkedIn-postauksissa |
| `ohjeet/uusi-postaus.md` | Ohje uuden postauksen tekemiseen |
| `tarkistus.py` | Lintteri, lukee säännöt tiedostosta |
| `postaukset/` | Luonnokset, yksi tiedosto per postaus |
| `out/` | Hyväksytyt leipätekstit ja kommentit |
| `.claude/skills/` | Claude Coden skillit |

## Skillit

| Skill | Milloin |
|---|---|
| `linkedin-luonnos` | Uusi postaus → `postaukset/DDMM-aihe.md` |
| `linkedin-tarkistus` | Tarkista olemassa oleva luonnos |
| `julkaisuvalmius` | Tarkista valmis teksti ennen julkaisua |

## Uusi postaus

1. Lue [ohjeet/uusi-postaus.md](ohjeet/uusi-postaus.md)
2. Claude Code: `tee uusi postaus aiheesta X, päivä DDMM`
3. Lintteri ajetaan automaattisesti skillin jälkeen
4. Ihminen muokkaa → git diff → hyväksyntä → `out/`

## Lintteri

```sh
python3 tarkistus.py postaukset/2608-kampanja.md
```

Lintteri raportoi kielletyt sanat rivinumeroineen. Se ei korjaa tekstiä —
korjaukset tehdään käsin ja git diff näyttää muutokset.

## Claude Code

Avaa projekti Claude Codessa. Se lukee `CLAUDE.md`:n automaattisesti.

Esimerkkejä:

```
tee uusi postaus aiheesta dev-työkalut markkinoinnissa, päivä 0109
tarkista postaukset/2608-kampanja.md
tarkista out/2608-kampanja.txt
```

## Git

Commit-historia näyttää miten säännöt ja postaukset kehittyvät ajan myötä.
Uusi sääntö on yksi rivi `saannot.md`:ssä — lintteri lukee sen seuraavalla
ajolla ilman koodimuutosta.
