# wb-country-stats

`wb-country-stats` is a tool which queries World Bank country statistics and dumps
the data as, for example, CSV.

Examples:

``` shell
$ wb-country-stats --list-countries | head
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
$ wb-country-stats --list-indicators 'urban population,.*of total'
JI.POP.URBN.ZS                      | Urban population, total (% of total population)
SP.URB.TOTL.FE.ZS                   | Urban population, female (% of total)
SP.URB.TOTL.MA.ZS                   | Urban population, male (% of total)
```


## Installation

- install `wb-country-stats` via _pipx_ (you can use _Mise_ to install _pipx_):
  ``` shell
  mise user -g pipx  # optional
  ```
  ``` shell
  pipx install git+https://github.com/jirib/wb-country-stats.git
  ```

## Development

- Mise
  * Linux (any)
    ``` shell
    curl https://mise.run | sh
    ```
  * Windows
    - (powershell)
      ```
      Set-ExecutionPolicy RemoteSigned -scope CurrentUser
      ```
      ```
      (irm https://astral.sh/uv/install.ps1) -replace '\bexit\b', '#exit removed' | iex
      ```
- Python development environment
  ``` shell
  mise install
  ```
  ```
  uv run wb-country-stats --help
  ```

  For development under _Visual Studio Code_ the following file might be helpful for debugging:

  ``` shell
  $ cat .vscode/launch.json
  {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug wb-country-stats (module)",
            "type": "debugpy",
            "request": "launch",
            "module": "wb_country_stats",
            "args": ["--list-indicators"],
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```