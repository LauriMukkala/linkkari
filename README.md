# Linkkari

Qalmarin LinkedIn-sisältödemon pohja. Näyttää miten git, CLAUDE.md, skillit
ja yksinkertainen lintteri tukevat postausten kirjoittamista.

Esitys: [git-lint-skillit](../esitykset/git-lint-skillit/index.html)

## Rakenne

| Tiedosto | Tehtävä |
|---|---|
| `CLAUDE.md` | Pysyvät ohjeet Claude Codelle |
| `saannot.md` | Kielletyt sanat, korvaukset ja rajat |
| `tarkistus.py` | Lintteri, lukee säännöt tiedostosta |
| `postaukset/` | Luonnokset, yksi tiedosto per postaus |
| `out/` | Hyväksytyt leipätekstit ja kommentit |
| `.claude/skills/` | Claude Coden skillit tarkistukseen |

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
tarkista postaukset/2608-kampanja.md
```

Skill `linkedin-tarkistus` palauttaa kentät KOUKKU, POIKKEAMAT, MITAT,
TOISTO ja KYSYMYS. Skill `julkaisuvalmius` tarkistaa valmiin tekstin
`out/`-kansiosta ennen julkaisua.

## Git

Commit-historia näyttää miten säännöt ja postaukset kehittyvät ajan myötä.
Uusi sääntö on yksi rivi `saannot.md`:ssä — lintteri lukee sen seuraavalla
ajolla ilman koodimuutosta.
