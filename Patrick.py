from openai import OpenAI
import streamlit as st

with st.sidebar:
    base_url =  st.text_input("Local URL",       value="http://localhost:1234/v1")
    api_key  =  st.text_input("API Key",         value="lm-studio")
    model    =  st.text_input("Model Name",      value="NousResearch/Hermes-2-Pro-Mistral-7B-GGUF")
    
    prompt   =  st.text_area("Assistant Prompt", 
                             value="""Always answer according to financial data and economic terms. 
Always follow these basic instructions when you answer:
1) You are a financial assistant.
2) Always provide sort answers.
3) Always be as accurate as possible.
4) Always if you do not know the right answer say that You Cannot Help.
""")
    
    "[LM Studio](https://lmstudio.ai/)"
    "[Source Code](https://github.com/arisdask/ai_project)"


st.title("🍻 Patrick 🍻")
st.caption("👶 An adaptable, open-source assistant bot to serve your unique requirements!")
st.caption("🧾 Preaty please, always double check the results.")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What would you like to discus today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if user_prompt := st.chat_input():
    if not api_key or not base_url or not model:
        st.info("Please check your Local URL, API Key and Model Name.")
        st.stop()

    from openai import OpenAI

    # Point to the local server
    client = OpenAI(base_url=base_url, api_key=api_key)

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.chat_message("user").write(user_prompt)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "assistant", "content": prompt},
            {"role": "user",      "content": user_prompt}
        ],
        temperature=0.1,
    )

    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)