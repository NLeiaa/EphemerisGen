🌌 Welcome to EphemerisGen

👤 Author: NLeiaa

🔗 GitHub: https://github.com/NLeiaa

> Select your language | [English](https://github.com/NLeiaa/EphemerisGen/blob/main/README/README.en.md) | [PtBr](https://github.com/NLeiaa/EphemerisGen/blob/main/README/README.br.md) |


# EphemerisGen

**EphemerisGen** is a Python tool for generating and querying astronomical ephemerides, calculating the positions of the main celestial bodies (Sun, Moon, planets) in zodiac signs for specific years or months. It allows exporting the data in JSON and CSV formats.

---

## Table of Contents

- [Overview](#overview)
- [Requirements and Installation](#requirements-and-installation)
- [How to Use](#how-to-use)
- [Example of Use](#example-of-use)
- [Screenshot](#screenshot)
- [Contributions](#contributions)
- [License](#license)

---

## Overview

**EphemerisGen** generates astronomical ephemerides for an entire year or a specific month, showing the zodiac positions of the main celestial bodies, as well as the sidereal time for each day.

---

## Requirements and Installation

- Python 3.7 or higher
- The [`ephem`](https://pypi.org/project/ephem/) library

### Installing the library

```bash
pip install ephem
```

Clone the repository or download the files to your computer.

---

## How to Use

Run the main script:

```bash
python main.py
```

Choose to query by:

- `y`: Full year  
- `m`: Specific month

After the query, choose to export the data in:

- `json`
- `csv`

---

## Project Structure

| File                     | Description                                             |
|--------------------------|---------------------------------------------------------|
| `main.py`                | Main script that starts the menu and directs queries    |
| `EphemerisGen_year.py`   | Generates and exports ephemerides for an entire year    |
| `EphemerisGen_month.py`  | Generates and exports ephemerides for a specific month  |

---

## Example of Use

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

... [ephemerides displayed] ...

Export data to JSON or CSV? (json/csv): json

✅ JSON export completed: ephemeris.json

Do you want to perform another consultation? (y/n): n

👋 Goodbye!
```

---

## Screenshot
![Screenshot](/Screenshot/EphemerisGen.png)

---

## Contributions

Contributions are welcome! If you have any suggestions for improvements or want to fix an issue, feel free to open an **issue** or send a **pull request**.

- **Issues**: Report any problems or suggestions [here](https://github.com/NLeiaa/EphemerisGen/issues).
- **Pull Requests**: Feel free to submit a pull request with improvements or fixes.

Remember to follow best practices when contributing and test your changes to ensure the code continues working as expected.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
