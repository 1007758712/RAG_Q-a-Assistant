import time
import streamlit as st
from rag import RagService
import config_data as config


st.title("文档智能问答")
st.divider()    #分隔符

if "message" not in st.session_state:
    st.session_state["message"] = [{"role":"assistant","content":"你好，有什么可以帮助你"}]
if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()


for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

prompt=st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role":"user","content":prompt})

    ai_re_list = []
    with st.spinner("AI思考中..."):
        res_stream = st.session_state["rag"].chain.stream({"input":prompt},config.session_config)

        def capture(generator , cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res_stream,ai_re_list))
        st.session_state["message"].append({"role": "assistant", "content":"".join(ai_re_list)})


    # res = RagService().chain.invoke({"input":"我研究遥感，推荐具体研究方向"},session_config)
    # print(res)



