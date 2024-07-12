# b15py

Ein Module um das B15F-Board mit Python zu programmieren
Dies ist ein Python Module für den B15F-Treiber.

> [!WARNING]
> Dieses Module funktioniert nur, wenn man die nötigen B15F-Headers installiert hat.
> Diese Installation ist gerade nur auf Debian durch den Installationsscript und Arch durch `yay b15f-git` möglich.
> ... zumindest solange niemand einen workaround findet.

## Installation

`pip install b15f`
oder
```bash
git clone https://www.github.com/mmeiler-dev/b15py
cd b15py
pip install .
```

## Benutzung

Hier folgt ein simples Beispiel von dem Module

```py
from b15py import B15F

def main():
  drv = B15F.getInstance()

  drv.analogWrite0(1023)
  print(drv.analogRead0())

if __name__ == "__main__":
  main()
```
