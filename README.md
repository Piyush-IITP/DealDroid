# DealDroid: The AI Shopping Agent

> **Project for [Droidrun DevSprint] 2026** > *Your Personal Autonomous Shopping Assistant powered by DroidRun.*

---

## 🚀 Overview
**DealDroid** is an intelligent Android automation agent that solves the hassle of manually checking multiple apps for the best price. 

Instead of opening Amazon, Flipkart, and Myntra one by one, simply tell DealDroid what you want. It wakes up, hunts down the product across all platforms, **Compares prices**,**Add to cart** and sends a detailed **WhatsApp Report** to your phone.

## ✨ Key Features
* **⚡ Flash Speed Search:** Uses direct Android Deep Links (ADB) to skip manual navigation and jump straight to search results.
* **📱 Multi-App Support:** Seamlessly navigates **Amazon**, **Flipkart**, and **Myntra**.
* **🛒 Auto-Add to Cart:** Intelligently identifies "Add to Cart" buttons using XML analysis and secures the item.
* **📊 Smart Comparison:** Reads prices and ratings using OCR/Text extraction to find the best deal.
* **💬 WhatsApp Reporting:** Sends a beautifully formatted mission report directly to your chat.
* **🧠 Gemini Powered:** Utilizes **Google Gemini 2.5 Flash/pro** for high-speed, low-latency decision making.

---
## 🛠️ Tech Involved
* **Core Logic:** Python 3.13+
* **AI Brain:** Google Gemini API (Gemini 2.5 Flash/Pro)
* **Agent Framework:** [DroidRun](https://github.com/droidrun/droidrun)
* **Device Control:** ADB (Android Debug Bridge)
* **Package Manager:** `uv` (for lightning-fast dependency management)

---
## 📸 Demo
[![DealDroid Demo](https://img.youtube.com/vi/3mmDZM8EvTQ/0.jpg)](https://youtu.be/3mmDZM8EvTQ)

---
## 🏃‍♂️ How to Run It
You'll need an Android phone (or emulator) and a Google API Key.

1.  **Clone this repo:**
    ```bash
    git clone [https://github.com/PiyushKumar/DealDroid.git](https://github.com/PiyushKumar/DealDroid.git)
    cd DealDroid
    ```

2.  **Install the dependencies:**
    (I used `uv` because it's way faster than pip, but pip works too).
    ```bash
    pip install uv
    uv sync
    ```

3.  **Add your API Key:**
    Create a file named `.env` and paste your key inside:
    ```
    GOOGLE_API_KEY=your_key_here
    ```

4.  **Run it:**
    Make sure your phone is plugged in, then:
    ```bash
    uv run main.py
    ```

---



