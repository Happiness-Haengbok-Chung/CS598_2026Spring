# 🌈 Building The Part of Lifelong Agents: 
# Supplemented Hallucination Detection / Behavior Planning Benchmark Dataset Construction

## 🙇‍♀️ Appreciation for the Supervision
> This project is developed under the supervision of Professor Dilek Hakkani-Tur and Takyoung Kim (TA) in the class "CS598 Conversational AI" at University of Illinois Urbana-Champaign (UIUC).
> And the key initial insight for this project is from Professor Bohyung Han & Professor Jae Sung Lee at Seoul National University (SNU).

## 🌟 Topics
- Supplementing the standard of the detrimental hallucination standard
- Constructing a robotic long-horizon motion planning benchmark dataset based on natural language

## 🔥 Folder contents
- ✅ Dataset: dataset used for this project
- ✅ Eval_models: functions that detect the hallucination with commercial large multimodal models (Gemini, ChatGPT, Grok)
- ✅ Prompts: prompts used for the hallucination detection and dataset construction
- ✅ Results_JSON: archive of the JSON files of the detrimental hallucination detection
- ✅ Results_graph: archive of the plots of the hallucination detection

## 📖 Key Reference
- Chen, Kedi, et al. "Diahalu: A dialogue-level hallucination evaluation benchmark for large language models." Findings of the Association for Computational Linguistics: EMNLP 2024. 2024.
- Li, Junyi, et al. "Halueval: A large-scale hallucination evaluation benchmark for large language models." Proceedings of the 2023 conference on empirical methods in natural language processing. 2023.

## 🚀 Installation & Reproduce

```bash
# 1. Clone repository
git clone https://github.com/Happiness-Haengbok-Chung/CS598_2026Spring.git

# 2. Install dependent libraries
pip install -r requirements.txt

# 3. Execution
python Eval_models/gemini_eval.py
```
