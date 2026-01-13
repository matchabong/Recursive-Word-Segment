# Recursive-Word-Segment
A Python utility that takes a continuous string of characters (without spaces) and segments it into valid English words using a recursive backtracking algorithm and a predefined dictionary.

## 📝 Description

This program solves the "Word Break" problem. It takes an input string like `THEYAREHAPPY` and attempts to reconstruct the sentence `THEY ARE HAPPY` by matching substrings against a hardcoded internal library of words.

If the string cannot be perfectly segmented into known words, or if it contains invalid characters, the program returns `Nonsense`.

## 🚀 Features

* **Recursive Backtracking**: Uses recursion to explore possible word splits.
* **Input Validation**: Automatically rejects numbers, symbols, and lowercase letters.
* **Custom Dictionary**: Includes a manually segmented library of common English nouns, verbs, pronouns, and adjectives.

## 🛠️ Getting Started

### Prerequisites
* Python 3.6

### How to Run
1.  Open your terminal.
2.  Run the script:
    ```bash
    python "workseg.py"
    ```
3.  Enter your **Uppercase** text string when the cursor appears.

## 📖 Usage Examples

**Important:** The input must be in **ALL CAPS**.

### ✅ Successful Case
Input:
```text
THEYAREHAPPY
