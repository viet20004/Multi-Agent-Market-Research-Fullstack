import os
from app_graph import market_research_graph

# Nhớ set API Key trước khi chạy nhé bạn
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

if __name__ == "__main__":
    print("--- BẮT ĐẦU CHẠY AI AGENT SYSTEM ---")

    # Input ban đầu cung cấp cho START node
    initial_input = {
        "topic": "Thị trường xe điện tại Việt Nam năm 2026",
        "logs": ["🚀 Hệ thống bắt đầu kích hoạt..."]
    }

    # Chạy đồ thị
    final_state = market_research_graph.invoke(initial_input)

    print("\n--- LỊCH SỬ LOGS (Dùng để stream lên Frontend) ---")
    for log in final_state["logs"]:
        print(log)

    print("\n--- BÁO CÁO CUỐI CÙNG (MARKDOWN) ---")
    print(final_state["report"])