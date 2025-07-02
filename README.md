===============================
🧠 Terminal Quiz Game (Python)
===============================

This is a simple terminal-based quiz game written in Python.

Features:
---------
✅ Loads questions from a JSON file  
✅ Supports multiple-choice and true/false questions  
✅ Randomized question and answer order  
✅ Tracks and saves user scores  
✅ Displays feedback after each answer  
✅ Increases difficulty after 10 questions  
✅ Shows current question progress  
✅ Optional timer for each question  

--------------------------
📂 File Structure
--------------------------

- quiz_game.py        → Main Python quiz program  
- questions.json      → Question bank (customizable)  
- scores.txt          → Stores results after each quiz  
- README.txt          → You're reading it!  

--------------------------
🛠 How to Use
--------------------------

1. Ensure you have Python 3 installed.

2. Customize `questions.json` with your own questions.
   Example format:

   [
     {
       "question": "What is 2 + 2?",
       "options": ["3", "4", "5", "6"],
       "answer": "4",
       "difficulty": "easy"
     },
     {
       "question": "What is the square root of 256?",
       "options": ["14", "16", "18", "20"],
       "answer": "16",
       "difficulty": "hard"
     }
   ]

3. Run the game from the terminal:

   ```bash
   python quiz_game.py

4. Answer questions within the time limit (default: 15 seconds per question).

5. After 10 questions, the quiz will switch to harder questions automatically.

6. Final scores are saved to scores.txt automatically.
