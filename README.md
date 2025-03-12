# 🤖 AI Chat Interface

A modern, responsive AI chat interface built with Streamlit and powered by Groq's LLM through LangChain. This application demonstrates the integration of cutting-edge AI capabilities in a user-friendly environment.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)

## 🌟 Features

- 🎨 Modern, dark-themed UI with responsive design
- 💬 Real-time chat interface with Groq's LLM
- 🔄 Persistent chat history
- 🎯 Clean and intuitive user experience
- 🛡️ Secure API key handling
- 📱 Mobile-friendly design

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- UV package manager (recommended)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MuhammadRaffey/streamlit-getting-started.git
cd streamlit-getting-started
```

2. Create and activate a virtual environment:

```bash
uv venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies using UV:

```bash
uv sync
```

4. Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

### Running the Application

Start the Streamlit app:

```bash
streamlit run src/streamlit_getting_started/main.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 💻 Usage

1. Enter your message in the text input field
2. Click the "Send" button or press Enter to send your message
3. The AI will process your message and respond in real-time
4. Your conversation history is maintained throughout the session

## 🛠️ Technology Stack

- **Frontend Framework**: Streamlit
- **AI Integration**: LangChain
- **Language Model**: Groq (Mixtral-8x7B-32768)
- **Styling**: Custom CSS
- **Environment Management**: Python dotenv

## 📝 Project Structure

```
ai-chat-interface/
├── src/
│   └── streamlit_getting_started/
│       └── main.py
├── .env
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/ai-chat-interface/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Muhammad Raffey**

- Portfolio: [https://raffey-portfolio.vercel.app/](https://raffey-portfolio.vercel.app/)
- GitHub: [@MuhammadRaffey](https://github.com/MuhammadRaffey)

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- LangChain for the LLM integration capabilities
- Groq for providing the powerful language model
