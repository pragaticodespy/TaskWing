
# TaskWing: Nightwing-Inspired Local AI Task Manager

**TaskWing** is a command-line AI assistant that channels the strategic leadership of **Nightwing** to help individuals and teams tackle work efficiently. Whether you're flying solo or coordinating a crew, TaskWing reads your task briefs from plain text and returns a mission-ready plan: assigned roles, suggested tools, estimated deadlines, and motivational banter to keep the team going.

---

## 📊 What Can TaskWing Do?

* Read plain `.txt` input describing solo or team-based tasks
* Interpret team member names and roles for intelligent delegation
* Generate **step-by-step task plans**, with tools/platforms to use
* Estimate **realistic deadlines and durations**
* Output Nightwing-style motivational quips for each subtask
* All responses are generated **locally** via **Ollama**, with no API dependencies

---

## 🛠️ Tech Stack

* **Language Model**: Ollama (`TaskWing:latest`)
* **Input Format**: Plain text task briefs
* **Logging**: Python `logging` for runtime updates
* **Interface**: CLI-based, zero UI, zero APIs

---

## 🔄 How It Works

```python
1. Read a text file with team roles and project goals
2. Parse and structure tasks
3. Send a structured prompt to the local LLM
4. Generate actionable plans (delegated, time-stamped, and tool-suggested)
5. Print the result to CLI and save to a .txt logbook
```

---

## 🎯 Example Input

```txt
Nightwing, we are a team. Our team consists of Anna, Olga, Jenna, Athena, and Lola.
Anna - Content Creator - uses Instagram, Canva, and TikTok.
Olga - Editor - uses Adobe and DaVinci Resolve.
Jenna - Graphic and Web Designer - uses Figma and VS Code
Lola - Software Developer and Web Designer - Programming Languages and VS Code
Athena - Chief Executive Officer
The task is to prepare a presentation for clients to attract investors. Include:
- Social media growth report by Anna, edited by Olga.
- Visual slides by Jenna.
- Software demo by Lola.
- Investor pitch by Athena.
Deadline: One week.
```

```txt
Help me Nightwing, I am solo on this mission.
help me get through these concepts, with my finish time - a week. Help me manage my time, please.

1. Artificial Neural Networks 
2. Convolution Neural Networks
3. Recurrent Neural Networks
4. Stochastic Gradient
```


## 🔹 Run It Yourself

1. Clone the repo
2. Add your `tasks.txt` in the `/data/` directory
3. Run `python taskwing.py`
4. Output appears in `agent37_logbook.txt`

---

## 🚀 Why I Built This

Tired of lifeless task managers, I created TaskWing to think like a strategic leader. Inspired by Nightwing’s calm, team-first approach, this tool helps solo workers and teams get moving with real deadlines and no guesswork.

---

## 📅 Status

**Project: Active, Functional**

**Built as**: A portfolio CLI product for LLM-based productivity

**Next Up**: Optional web UI, voice assistant overlay, and time tracking

---

Made for builders who like banter. 🕷️


# Here's the sample output as shown:

<img width="960" alt="team-1" src="https://github.com/user-attachments/assets/85717b62-2316-44ca-9995-26e2e258154f" />

<img width="960" alt="team-3" src="https://github.com/user-attachments/assets/60f821a2-da73-4c8b-a87a-b01b2e83fb9b" />

<img width="960" alt="team-2" src="https://github.com/user-attachments/assets/b35254ba-919e-412a-aaa4-3c8d30c82ce2" />

and for the solo, 

<img width="960" alt="solo-3" src="https://github.com/user-attachments/assets/50382936-2b2c-47ad-833b-e840bb56594e" />

<img width="960" alt="solo-2" src="https://github.com/user-attachments/assets/9c4508ac-88df-49f8-8d8c-eb2189005fa0" />

<img width="960" alt="solo-1" src="https://github.com/user-attachments/assets/459d20bb-c0ed-473a-8e24-0fb1829fdbf2" />


