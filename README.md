```md
assistant/
│
├── main.py
│
├── core/                     # 🔒 STABLE CORE (rarely changed)
│   ├── engine.py             # Main execution loop
│   ├── router.py             # Intent → plugin routing
│   ├── intent.py             # Intent detection logic
│   ├── safety.py             # All hard safety rules
│   ├── context.py            # Runtime state (session memory)
│   └── registry.py           # Plugin discovery & validation
│
├── plugins/                  # 🔌 ALL FEATURES LIVE HERE
│   ├── open_app.py
│   ├── file_search.py
│   ├── memory_store.py
│   ├── memory_recall.py
│   ├── reminder_scheduler.py
│   ├── web_fetch.py
│   └── future_plugin.py
│
├── llm/                      # 🧠 MODEL INTERACTION (NO ACTIONS)
│   ├── client.py             # OpenAI / Gemini / local model wrapper
│   ├── prompts.py            # Structured prompts
│   ├── critique.py           # Self-critique & improvement loop
│   └── ranking.py            # Option ranking / evaluation
│
├── tools/                    # 🛠️ REAL-WORLD ACTIONS (CONTROLLED)
│   ├── filesystem.py         # Safe file & folder ops
│   ├── shell.py              # Restricted command execution
│   ├── browser.py            # Web / real-time data
│   └── scheduler.py          # Time-based reminders
│
├── memory/                   # 🧠 LOCAL MEMORY (STRUCTURED)
│   ├── short_term.json       # Current session info
│   ├── long_term.db          # SQLite memory store
│   ├── reminders.db          # Scheduled reminders
│   └── patterns.json         # What you often forget (optional)
│
├── input/                    # 🎤 INPUT HANDLERS
│   ├── text.py
│   └── voice.py
│
├── output/                   # 🔊 OUTPUT HANDLERS
│   ├── text.py
│   └── voice.py
│
├── config/                   # ⚙️ SYSTEM RULES & SETTINGS
│   ├── settings.yaml
│   ├── permissions.yaml
│   ├── protected_paths.yaml
│   └── plugins.yaml
│
├── logs/                     # 📜 DEBUGGING & TRACEABILITY
│   └── assistant.log
│
└── PROJECT_CHARTER.txt       # 🧭 SOURCE OF TRUTH
```