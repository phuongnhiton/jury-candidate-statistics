# Academic Jury & Candidate Statistics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Data Analysis](https://img.shields.io/badge/Focus-Statistics-green.svg)
![Pickle](https://img.shields.io/badge/Storage-Pickle-lightgrey.svg)

An analytical tool designed to process academic competition data and identify statistical correlations between candidate profiles and admission outcomes. The project explores potential biases or trends related to gender, university affiliation, and jury composition.

---

## Overview
This project processes raw candidate data and jury lists to answer critical questions about academic admissions:
* **Success Rates:** Calculating the overall probability of admission.
* **Affiliation Bias:** Comparing success rates of candidates from different universities (e.g., Paris 1 vs. Rennes 1).
* **Network Effect:** Analyzing if having a thesis director in the jury correlates with a higher admission probability.
* **Gender Analysis:** Checking for statistical differences in admission rates between male and female candidates.

## Tech Stack
| Tool | Purpose |
| :--- | :--- |
| **Python** | Core logic for data processing and calculation |
| **Pickle** | Handling serialized binary databases (`BaseCandidat`, `BaseJury`) |
| **CSV Engine** | Custom implementation to export structured data for external tools |
| **String Parsing** | Advanced splitting and cleaning of unstructured `.txt` profiles |

## Project Structure
```text
├── InformationCandidats/  # Directory containing raw text profiles
├── csv_generator.py       # Converts binary/text data to a clean CSV
├── statistics.py          # Core statistical calculation engine
├── Output.py              # Advanced conditional analysis & reporting
└── data.csv               # The final structured output for analysis

This project is for educational and statistical research purposes only. It aims to demonstrate data processing capabilities and does not imply any real-world bias without further academic validation.
