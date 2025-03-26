import gradio as gr
from rag_core import LegalRAGSystem

# Initialize RAG system
DOCUMENT_PATH = "legal-doc/case-file.pdf"
rag_system = LegalRAGSystem(DOCUMENT_PATH)

css = """
@import url('https://fonts.googleapis.com/css2?family=Headland+One&display=swap');

:root {
    --bg: #f5f5f7;
    --card-bg: #ffffff;
    --text: #1d1d1f;
    --accent: #0066cc;
    --border: #d2d2d7;
    --radius: 12px;
    --font-heading: 'Headland One', serif;
    --font-body: -apple-system, BlinkMacSystemFont, sans-serif;
}
body {
    font-family: var(--font-heading);
    background: var(--bg) !important;
}
h1, h2, h3, h4 {
    font-family: var(--font-heading) !important;
    font-weight: 400 !important;
}
.gr-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
}
.gr-box {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    margin-bottom: 20px;
}
.gr-input, .gr-textbox {
    border-radius: var(--radius);
    padding: 12px 16px;
    font-family: var(--font-heading);
}
.gr-button {
    background: var(--accent) !important;
    color: white !important;
    border-radius: var(--radius) !important;
    font-family: var(--font-heading) !important;
}
.chatbot {
    min-height: 400px;
    font-family: var(--font-heading);
}
.signature {
    text-align: center;
    margin-top: 20px;
    color: #666;
    font-family: var(--font-heading);
}
.signature a {
    color: var(--accent);
    text-decoration: none;
}
.signature a:hover {
    text-decoration: underline;
}
"""

def respond(question, chat_history):
    chat_history.append({"role": "user", "content": question})
    answer = rag_system.query(question)
    chat_history.append({"role": "assistant", "content": answer})
    return chat_history, ""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""<h1 style="font-family: 'Headland One', serif">Legal Document Assistant</h1>""")
    
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                label="Chat History",
                container=True,
                height=500,
                type="messages"
            )
            question = gr.Textbox(
                label="Your Question",
                placeholder="Ask about clauses or terms...",
                lines=2
            )
            with gr.Row():
                submit = gr.Button("Submit", variant="primary")
                clear = gr.Button("Clear", variant="secondary")

        with gr.Column(scale=1):
            gr.Markdown("""<h3 style="font-family: 'Headland One', serif">Current Document</h3>""")
            gr.File(
                value=DOCUMENT_PATH,
                interactive=False,
                label=None
            )
            gr.Markdown("""
            <h4 style="font-family: 'Headland One', serif">How to Use</h4>
            <ol>
            <li>Ask about specific clauses</li>
            <li>Request explanations</li>
            <li>Compare sections</li>
            </ol>
            """)
            
            gr.HTML("""
            <div class="signature">
                Made with ❤️ by <a href="https://www.linkedin.com/in/tharunikal" target="_blank">Tharunika L</a>
            </div>
            """)

    submit.click(
        respond,
        [question, chatbot],
        [chatbot, question]
    )
    clear.click(lambda: [], None, chatbot)
    question.submit(
        respond,
        [question, chatbot],
        [chatbot, question]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=True
    )