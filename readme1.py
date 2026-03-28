"""""
if "service" not in st.session_state:
    st.session_state["service"]=KnowledgeBaseService()
st.session_state["service"].upload_by_str(text,file_name)
防止重复创建KnowledgeBaseService

代码运行方式：在新建环境中进入文件所在地运行 streamlit run app_file_uploader.py

"""""