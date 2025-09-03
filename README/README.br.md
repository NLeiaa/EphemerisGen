🌌 Bem vindo(a) ao EphemerisGen

👤 Autor: NLeiaa

🔗 GitHub: https://github.com/NLeiaa

> Selecione seu idioma | [English](https://github.com/NLeiaa/EphemerisGen/blob/main/README/README.en.md) | [PtBr](https://github.com/NLeiaa/EphemerisGen/blob/main/README/README.br.md) |


# EphemerisGen

**EphemerisGen** é uma ferramenta em Python para geração e consulta de efemérides astronômicas, calculando as posições dos principais corpos celestes (Sol, Lua, planetas) em signos do zodíaco para anos ou meses específicos. Permite exportar os dados em formatos JSON e CSV.

---

## Índice

- [Visão Geral](#visão-geral)
- [Requisitos e Instalação](#requisitos-e-instalação)
- [Como Usar](#como-usar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Screenshot](#screenshot)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## Visão Geral

**EphemerisGen** gera efemérides astronômicas para um ano inteiro ou um mês específico, mostrando as posições zodiacais dos corpos celestes principais, além do tempo sidéreo para cada dia.

---

## Requisitos e Instalação

- Python 3.7 ou superior
- Biblioteca [`ephem`](https://pypi.org/project/ephem/)

### Instalação da biblioteca

```bash
pip install ephem
```

Clone o repositório ou baixe os arquivos para o seu computador.

---

## Como Usar

Execute o script principal:

```bash
python main.py
```

Escolha consultar por:

- `y`: Ano completo  
- `m`: Mês específico

Após a consulta, opte por exportar os dados em formato:

- `json`
- `csv`

---

## Estrutura do Projeto

| Arquivo                  | Descrição                                                  |
|--------------------------|------------------------------------------------------------|
| `main.py`                | Script principal que inicia o menu e direciona as consultas |
| `EphemerisGen_year.py`   | Geração e exportação de efemérides para um ano completo     |
| `EphemerisGen_month.py`  | Geração e exportação de efemérides para um mês específico   |

---

## Exemplo de Uso

```bash
$ python main.py

/*
 *      ______       _                              _      _____
 *     |  ____|     | |                            (_)    / ____|
 *     | |__   _ __ | |__   ___ _ __ ___   ___ _ __ _ ___| |  __  ___ _ __  
 *     |  __| | '_ \| '_ \ / _ \ '_ ` _ \ / _ \ '__| / __| | |_ |/ _ \ '_ \ 
 *     | |____| |_) | | | |  __/ | | | | |  __/ |  | \__ \ |__| |  __/ | | |
 *     |______| .__/|_| |_|\___|_| |_| |_|\___|_|  |_|___/\_____|\___|_| |_|
 *            | |
 *            |_|
 *
 *              Astrological Ephemeris Generator · v1.0 🌌
 */
==================================================
🌌 Welcome to EphemerisGen
👤 Author: NLeiaa
🔗 GitHub: https://github.com/NLeiaa
==================================================

Consult by year or month? (y/m): y
Enter year (e.g., 2025): 2025

... [efemérides exibidas] ...

Export data to JSON or CSV? (json/csv): json

✅ JSON export completed: ephemeris.json

Do you want to perform another consultation? (y/n): n

👋 Goodbye!
```

---

## Screenshot
![Screenshot](/Screenshot/EphemerisGen.png)

---

## Contribuições

Contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria, ou quiser corrigir algum erro, fique à vontade para abrir uma **issue** ou enviar um **pull request**.

- **Issues**: Relate qualquer problema ou sugestão [aqui](https://github.com/NLeiaa/EphemerisGen/issues).
- **Pull Requests**: Sinta-se à vontade para enviar um pull request com melhorias ou correções.

Lembre-se de seguir as diretrizes de boas práticas ao contribuir e de testar suas mudanças para garantir que o código continue funcionando como esperado.

---

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais informações.
