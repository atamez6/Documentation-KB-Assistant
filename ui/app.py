import asyncio
from typing import Any,Dict,List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.chain import ask
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage





st.set_page_config(page_title="KB assitant", layout="centered")
st.title("Documentation Helper")

def __format__sources():
    pass


with st.sidebar:
    st.subheader("Session Active")
    if st.button("Clear chat", use_container_width=True):
        #save in a state
        st.session_state.pop("messages", None)
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content": "Ask me anything about your uploaded Docs and I'll retrieve most relevant information",
            "sources": [],

        }

    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
         st.markdown(msg["content"])
         if msg.get("sources"):
             with st.expander("Sources"):
                 for source in msg["sources"]:
                     st.markdown(f"-- {source}-- ")


prompt = st.chat_input("Ask me anything about your uploaded Docs and I'll retrieve most relevant information")

if prompt:
    history = []
    for msg in st.session_state.messages[1:]:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history.append(AIMessage(content=msg["content"]))
    st.session_state.messages.append({"role":"user","content":prompt,"sources":[]})

    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("getting info and creating a response"):
                pre_answer, serialized_docs = ask({"question": prompt}, history=history)
                answers= str(pre_answer.strip() or "(not answer to show.)")
                sources=serialized_docs

            st.markdown(answers)
            if sources:
                with st.expander("Sources"):
                    for source in sources:
                        filename = source["metadata"].get("source", "unknown")
                        preview = source["page_content"][:100]
                        st.markdown(f"📄 **{filename}**: {preview}...")
            st.session_state.messages.append(
                {"role":"assistant",
                "content":answers,
                "sources": sources}
            )            

        except Exception as e:
            st.error("Failed creating a response")
            st.exception(e)    