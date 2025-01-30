# Q&A Chatbot

A simple Q&A chatbot built using LangChain and Streamlit.

## 🚀 Features

- Uses LangChain for natural language processing
- Deployed on Streamlit for easy access
- Secure handling of API keys using `.env` and Streamlit secrets
- Supports two models: **Llama3-2** and **DeepSeek R1:1.15B**

## 🛠️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment

#### For Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```ini
LANGCHAIN_API_KEY="your_api_key_here"
LANGCHAIN_PROJECT="your_project_name_here"
```

Make sure this file is **not** included in version control by adding `.env` to `.gitignore`.

### 5️⃣ Run the Streamlit App

```sh
streamlit run app.py
```

## 🚀 Deployment on Streamlit Cloud

1. Push the project to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and select the branch.
4. Add secrets in **Streamlit Settings > Secrets**:
   ```ini
   LANGCHAIN_API_KEY="your_api_key_here"
   LANGCHAIN_PROJECT="your_project_name_here"
   ```
5. Deploy the app and access it online!

### 🌍 Live Demo

You can access the deployed app here: **[Streamlit App](https://simple-q-a-chatbot-nxmzpem7ysbmepahrwy9dk.streamlit.app/)**


