# AI Interview Buddy  
A Python CLI tool that helps you practice interview questions, get instant feedback, and track your progress - all from your terminal.

## Features
- **Single-question practice** with instant scoring & feedback  
- **3-question practice sessions** with summary stats  
- **Answer evaluation** (word count, filler words, action verbs, ownership)  
- **Review your last 5 answers**  
- **Clean terminal UI** powered by Rich

## Tech Stack
- Python 3  
- Rich (terminal UI)  
- Pytest (tests)  
- Datetime / simple text-based storage  

## Installation

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/ai-interview-buddy
cd ai-interview-buddy
```
Create a virtual environment:

```bash
python -m venv venv
```

Activate it:
- **Windows**
```bash
venv\Scripts\activate
```
- **Mac/Linux**
```bash
source venv/bin/activate
```

Running the App:
```bash
python app.py
```

Running Tests:
```bash
pytest
```