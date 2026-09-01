import re, sys, pathlib

sanat = pathlib.Path("saannot.md").read_text().split("# Rajat")[0]
kielletyt = re.findall(r"^(\S+)\s{2,}(.+)$", sanat, re.M)
rivit = pathlib.Path(sys.argv[1]).read_text().splitlines()

n = 0
for i, rivi in enumerate(rivit, 1):
    for sana, syy in kielletyt:
        alku = sana.rstrip("*")
        if re.search(r"\b" + alku + r"\w*", rivi, re.I):
            print(f'rivi {i:2}  VIRHE  "{alku}"  {syy}')
            n += 1

print(f"{n} huomiota. Tarkistus ei korjaa naita.")
