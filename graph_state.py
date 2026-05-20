from typing import TypedDict, Annotated, List
import operator

class ResearchState(TypedDict):
    topic: str                                 # Chủ đề người dùng nhập vào
    raw_data: str                              # Dữ liệu thô thu thập từ Internet
    analysis: str                              # Kết quả phân tích SWOT/Số liệu
    report: str                                # Báo cáo Markdown cuối cùng
    # operator.add giúp các Node ghi thêm log vào danh sách mà không làm ghi đè log cũ
    logs: Annotated[List[str], operator.add]