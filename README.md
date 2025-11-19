# 🧠 FitAI

### Personalized AI Health & Fitness App Powered by LLaMA3 (via Ollama) + FastAPI + LangChain

---

> "What if your personal trainer, dietician, and recovery expert lived in your browser and actually knew you?" — That’s Smart Fitness Coach.

Smart Fitness Coach is your all-in-one **AI-powered health assistant** — intelligently guiding you to better fitness, nutrition, recovery, and lifestyle habits through personalized plans generated in real time using your input.

Whether you're trying to lose fat, build muscle, sleep better, or learn what supplements actually work — this AI coach has got you.

---

## 💼 Why This Project Matters

- 🌍 **Health Crisis**: Over 1.9B adults are overweight, with over 650M obese
- 😓 **Misinformation**: Social media is flooded with influencer “bro-science”
- 🧠 **Decision Fatigue**: People don’t know what to eat, when to rest, or how to train
- 💸 **Unaffordable coaching**: Personal trainers & nutritionists are expensive

> We’re solving this with a local-first AI system that gives you everything a fitness coach would — for free, forever.

---

## 🙋‍♂️ Why I Built This

Working in the healthcare industry at **Johnson & Johnson** and **Novartis**, I saw firsthand how much data we have around wellness — and how little of it is accessible or actionable for individuals. 

I’ve always been personally committed to living a healthy, balanced life — I meditate daily, practice **pranayama** (yogic breathwork), train consistently, and follow a clean diet. These habits have transformed my energy, clarity, and mental strength.

I wanted to bring that clarity and discipline to others through a **powerful, personalized AI fitness assistant** — something that combines scientific accuracy with holistic guidance.

This project is my way of merging industry-grade health intelligence with accessible tools that can actually make people’s lives better.

> **This isn’t just a project. It’s a movement.**
> Millions of people don’t need more gym selfies. They need guidance.
> This app brings that — with zero cost, infinite personalization, and zero judgment.

---

## 🚀 Features

| Domain         | What It Does                                                                 |
|----------------|------------------------------------------------------------------------------|
| 🏋️ Workouts     | Suggests personalized training splits, full-body, cardio, or strength plans |
| 🥗 Nutrition     | Gives calorie goals, protein intake, sample meals, and macro tracking tips |
| 😴 Recovery      | Tracks sleep advice, stress management, and active recovery routines       |
| 💊 Supplements   | Recommends evidence-backed supplements (creatine, whey, etc.)              |
| 📊 Visual Plans | Generates **weekly workout tables** using Plotly.js                        |
| ⚡️ Instant Chat | Ask anything — your AI coach remembers your level, stress, and sleep        |

---

## 🧠 How It Works

- Built with **FastAPI** for performance and modular endpoints
- Powered by **LLaMA3 via Ollama** — all runs **locally**, no OpenAI API needed
- Uses **LangChain + FAISS** for modular agent routing (1 agent per topic)
- Markdown files ingested and vectorized to power retrieval-based QA
- Visual output with **Plotly.js** (HTML frontend is fully customizable)

---

## 🏁 Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Visit [http://localhost:8000](http://localhost:8000) and type:

```txt
"Give me a 3-day fat loss workout"
"What should I eat before lifting?"
"Show me my weekly workout table"
```

---

## 💡 Vision: What's Next

We’re building the **world’s smartest, most personalized** open-source fitness brain:

- 🧬 **Body Type Adaptive Models**
- 📝 **Progress Tracking + Journaling**
- 🧘 **Mental Health Integration**
- 🧑‍⚕️ **Live Coaching Interface (GPT-4 Vision)**
- 🌐 **Multi-language support**
- ☁️ **Cloud & Mobile App Sync (optional)**

---

## 🔭 Future Scope

Here's how we plan to evolve Smart Fitness Coach into a full-fledged AI lifestyle platform:

- 📱 **Native Mobile App** – Seamless iOS & Android support for anywhere coaching
- 🧬 **Genetic-Based Fitness Adaptation** – Integrate with genomics APIs to tailor plans
- 🧮 **Auto Macro & Calorie Tracker** – Connect to OCR/scan features from meals
- 🤝 **Wearables Integration** – Sync with Apple Health, Garmin, Fitbit for real-time optimization
- 📖 **Content & Habit Coaching** – Add personalized micro-lessons for mindset and lifestyle change
- 🧪 **Fine-Tuning** – Train on curated fitness QA data for greater accuracy
- 🌎 **Voice Assistant Integration** – Use it via smart speakers or voice control
- 🧍‍♀️ **Community Sharing** – Build a private Discord-like community for fitness buddy systems

---

## 📈 Why Fund This?

- 🔓 Fully offline + local (no API or SaaS cost)
- 🧠 LLM-powered (can be fine-tuned for medical-grade use cases)
- 💰 Targets a massive market ($100B+ fitness & wellness industry)
- 📣 Social impact: democratizes access to health coaching

> Let’s build a **fitness intelligence layer** for every human — not just the top 1% with money and motivation.

---

## 🏢 Backed by Industry Insight

Built by a developer with experience at global healthcare leaders:
- ✅ Johnson & Johnson – Medical AI Research
- ✅ Novartis – Data Science in Clinical Innovation

---

## 👨‍💻 Made By

[Yash Pise](https://github.com/yp0505) — ML Engineer, Fitness Hacker, and Builder of AI that serves humanity. 

---

## 💸 Looking to Fund the Future of Health?

I'm open to strategic partnerships, angel investment, or co-founding opportunities with mission-aligned believers.

📬 Email: yashpise98@gmail.com

---

## 📬 Want to Collaborate?

Open an issue, fork the project, or message me directly. This is just the beginning 💥
