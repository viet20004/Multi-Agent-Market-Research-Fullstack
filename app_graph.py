from langgraph.graph import StateGraph, START, END
from graph_state import ResearchState
from nodes import researcher_node, analyst_node, writer_node

# 1. Khởi tạo đồ thị với State đã định nghĩa
workflow = StateGraph(ResearchState)

# 2. Thêm các Nodes vào đồ thị
workflow.add_node("researcher", researcher_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("writer", writer_node)

# 3. Kéo các đường nối (Edges) quy định luồng chạy
workflow.add_edge(START, "researcher")  # Điểm bắt đầu đi vào Researcher
workflow.add_edge("researcher", "analyst") # Xong Researcher sang Analyst
workflow.add_edge("analyst", "writer")     # Xong Analyst sang Writer
workflow.add_edge("writer", END)          # Kết thúc đồ thị

# 4. Biên dịch đồ thị thành một ứng dụng có thể chạy được
market_research_graph = workflow.compile()