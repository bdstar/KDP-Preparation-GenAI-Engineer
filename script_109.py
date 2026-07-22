# Gradio: wrap a model in a chat interface — a working web app in a few lines.
import gradio as gr
 
def respond(message, history):
    return generate_answer(message)          # your Part VI agent / RAG backend
 
gr.ChatInterface(fn=respond, title="Support Assistant").launch()   # interactive web UI
# Streamlit: a small data application around the same backend.
import streamlit as st
 
st.title("Document Assistant")
question = st.text_input("Ask a question about the docs:")
if question:
    answer, sources = rag_backend(question)        # your Part V RAG backend
    st.write(answer)
    with st.expander("Sources"):
        for s in sources:
            st.write(s)                            # richer layout than a bare chat
