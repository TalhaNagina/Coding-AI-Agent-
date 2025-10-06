# 🧠 Coding AI Agent

A **Python-based AI agent** that can understand natural language coding instructions, analyze files, read/write code, and even run Python scripts — all powered by the **Gemini API** and local tool functions.

This project demonstrates how to connect an LLM (Gemini) with real-world coding tools through **function calling**.  
It’s designed for learning and experimentation — not production use.

---

## 🚀 What It Does

Here’s what happens behind the scenes:

1. You give the agent a **coding request** in plain English — like *“add a function to calculate factorial”* or *“run calculator.py and show output.”*
2. The agent sends your request to **Gemini**.
3. Gemini decides which tool it needs — read, write, or run a file.
4. The selected tool runs locally (in the `calculator/` test folder).
5. The output is returned to Gemini, which then decides the next step.
6. The loop continues until the agent produces the final working code.

In short:  
**Prompt → Model → Function Call → Execution → Feedback → Result**

---

## 🧩 Features

- Uses **Gemini API** for natural language understanding.  
- Demonstrates **function calling** and tool chaining.  
- Reads, writes, and executes local Python code.  
- Modular design with `main.py` (orchestrator) and `call_function.py` (tool handler).  
- Includes a test project (`calculator/`) to safely experiment with code generation.

---

## 🗂️ Project Structure

```
Coding-AI-Agent/
│
├── main.py                # Main agent loop (Gemini communication)
├── call_function.py       # Handles function execution and responses
├── functions/             # Helper tools (get_file_content, run_python_file, etc.)
├── calculator/            # Example project for testing the AI agent
├── .env                   # Contains your GEMINI_API_KEY (not committed)
├── requirements.txt       # Project dependencies
└── README.md              # You’re reading it
```

---

## ⚙️ Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/TalhaNagina/Coding-AI-Agent-.git
cd Coding-AI-Agent-
```

### 2. Create a Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key
Create a `.env` file in the project root and add:
```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Agent

Run the main script:
```bash
python main.py
```

Then type a coding instruction, for example:
```
Add a new function in calculator.py to multiply two numbers.
Run calculator.py.
Show me the output.
```

The agent will automatically:
- Read your `calculator/` files
- Generate or modify code
- Execute the script
- Display the results

---

## 🧠 How It Works (Internals)

| Component | Role |
|------------|------|
| **main.py** | Core driver that talks to Gemini, sends/receives messages, and handles loops. |
| **call_function.py** | Executes local functions requested by Gemini (file ops, running code). |
| **functions/** | Contains definitions for each callable tool (read file, write file, run file, etc.). |
| **calculator/** | A small Python project used to safely test the AI agent’s actions. |

The agent can iterate multiple times (default `max_iter=20`) — it continues improving or testing code until it reaches a working result.

---

## ⚠️ Notes and Limitations

- This is an **educational project** — not a production-safe coding environment.  
- Avoid giving access to critical or personal directories. The agent is meant to operate in the `calculator/` sandbox.  
- Gemini might sometimes produce unexpected function calls; restart if the loop stalls.  
- Execution is local and not sandboxed — don’t run untrusted code.

---

## 💡 Example Interaction

```
User: Add a function in calculator.py to find factorial of a number.
Agent: Added factorial() function in calculator.py
User: Run calculator.py
Agent: Output -> Enter a number: 5
        Factorial: 120
```

---

## 🧰 Future Improvements

- Add safety sandbox for running model-generated code.  
- Improve conversation memory and context tracking.  
- Add a web or CLI interface for easier use.  
- Integrate multiple test projects beyond calculator.

---

## 🧑‍💻 Author

**Talha Nagina**  
B.Tech CSE Final Year | Nirma University  
[LinkedIn](https://www.linkedin.com/in/talhanagina) | [GitHub](https://github.com/TalhaNagina)

---

## 📝 License

MIT License — free to use, modify, and learn from.  
Just don’t expose your API keys publicly.
