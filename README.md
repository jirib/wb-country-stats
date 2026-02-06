# wb-country-stats

`wb-country-stats` is a tool which queries World Bank country statistics and dumps
the data as, for example, CSV.

Examples:

``` shell
$ uv run wb-country-stats --list-countries | head
AW | Aruba
ZH | Africa Eastern and Southern
AF | Afghanistan
A9 | Africa
ZI | Africa Western and Central
AO | Angola
AL | Albania
AD | Andorra
1A | Arab World
AE | United Arab Emirates
```

``` shell
$ uv run wb-country-stats --list-indicators 'urban population,.*of total'
JI.POP.URBN.ZS                      | Urban population, total (% of total population)
SP.URB.TOTL.FE.ZS                   | Urban population, female (% of total)
SP.URB.TOTL.MA.ZS                   | Urban population, male (% of total)
```
## Installation

- Mise
  * Linux (any)
    - `curl https://mise.run | sh`
  * Windows
    - (powershell) `Set-ExecutionPolicy RemoteSigned -scope CurrentUser`
    - (powershell) `(irm https://astral.sh/uv/install.ps1) -replace '\bexit\b', '#exit removed' | iex`
- clone this repo
- Python & UV
  * `mise install`
- Running graph.py (under normal user!)
  * `uv run wb-country-stats --help`