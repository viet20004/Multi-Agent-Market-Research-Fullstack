import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
# 1. Import thêm công cụ tìm kiếm của LangChain
from langchain_community.tools import DuckDuckGoSearchRun
from graph_state import ResearchState
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)

# Khởi tạo công cụ tìm kiếm
search_tool = DuckDuckGoSearchRun()


def researcher_node(state: ResearchState):
    """Agent 1: Cào dữ liệu từ Internet dựa trên Topic"""
    topic = state["topic"]

    # 2. Gọi Agent dùng công cụ ra ngoài Internet tìm kiếm thực tế
    print(f"\n[Đang tìm kiếm trên Internet]: {topic}...")
    try:
        # Search tool sẽ trả về các đoạn text chứa thông tin thực tế mới nhất
        real_web_data = search_tool.invoke(topic)
        log_msg = f"🤖 Researcher Agent: Đã cào dữ liệu THỰC TẾ từ Internet cho từ khóa '{topic}'."
    except Exception as e:
        real_web_data = f"Không thể tìm kiếm do lỗi: {str(e)}"
        log_msg = "🤖 Researcher Agent: Lỗi kết nối mạng, không cào được dữ liệu."

    return {
        "raw_data": real_web_data,  # Truyền dữ liệu thật cho Analyst phân tích
        "logs": [log_msg]
    }


# ... (Giữ nguyên analyst_node và writer_node ở phía dưới) ...
def analyst_node(state: ResearchState):
    """Agent 2: Phân tích dữ liệu thô thành thông tin có cấu trúc"""
    raw_data = state["raw_data"]

    prompt = ChatPromptTemplate.from_template(
        "Bạn là một chuyên gia phân tích thị trường. Hãy phân tích dữ liệu sau đây và tóm tắt các điểm chính (Ưu điểm, Nhược điểm, Cơ hội):\n\n{data}"
    )
    chain = prompt | llm
    response = chain.invoke({"data": raw_data})

    return {
        "analysis": response.content,
        "logs": ["📊 Analyst Agent: Đã phân tích xong dữ liệu thô và trích xuất mô hình thị trường."]
    }


def writer_node(state: ResearchState):
    """Agent 3: Viết báo cáo hoàn chỉnh dưới dạng Markdown"""
    topic = state["topic"]
    analysis = state["analysis"]

    prompt = ChatPromptTemplate.from_template(
        "Bạn là một copywriter chuyên nghiệp. Hãy chuyển đổi phần phân tích sau đây thành một bản báo cáo nghiên cứu thị trường chuyên nghiệp bằng Markdown cho chủ đề: {topic}.\n\nPhân tích:\n{analysis}"
    )
    chain = prompt | llm
    response = chain.invoke({"topic": topic, "analysis": analysis})

    return {
        "report": response.content,
        "logs": ["✍️ Writer Agent: Đã hoàn thành bản báo cáo Markdown cuối cùng."]
    }