import json
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app_graph import market_research_graph

app = FastAPI(title="AI Market Research Agent API")

# 1. Cấu hình CORS - Bắt buộc phải có để Frontend (Next.js) gọi API được
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong thực tế sản xuất sẽ đổi thành domain của Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Định nghĩa cấu trúc dữ liệu Request nhận từ Frontend
class ResearchRequest(BaseModel):
    topic: str


async def stream_agent_events(topic: str):
    """Async generator để stream dữ liệu về Frontend theo định dạng SSE"""
    initial_input = {
        "topic": topic,
        "logs": ["🚀 Hệ thống bắt đầu kích hoạt..."]
    }

    try:
        # Gửi log khởi tạo đầu tiên cho Frontend biết hệ thống đã nhận lệnh
        yield f"data: {json.dumps({'type': 'log', 'content': '🚀 Hệ thống bắt đầu kích hoạt...'}, ensure_ascii=False)}\n\n"
        await asyncio.sleep(0.2)  # Delay nhẹ để Frontend kịp render

        # Sử dụng .astream() của LangGraph để bắt các sự kiện bất đồng bộ
        async for event in market_research_graph.astream(initial_input, stream_mode="updates"):
            # Cấu trúc của event: {'node_name': {'field_1': value, 'logs': [...]}}
            for node_name, node_output in event.items():

                # 1. Nếu Node đó có trả về logs, stream log đó về Frontend ngay
                if "logs" in node_output:
                    for log in node_output["logs"]:
                        yield f"data: {json.dumps({'type': 'log', 'content': log}, ensure_ascii=False)}\n\n"

                # 2. Nếu là Writer Agent hoàn thành, stream toàn bộ bài báo cáo Markdown
                if node_name == "writer" and "report" in node_output:
                    yield f"data: {json.dumps({'type': 'report', 'content': node_output['report']}, ensure_ascii=False)}\n\n"

                await asyncio.sleep(0.1)

        # Gửi tín hiệu hoàn thành luồng cho Frontend đóng kết nối
        yield f"data: {json.dumps({'type': 'done'}, ensure_ascii=False)}\n\n"

    except Exception as e:
        yield f"data: {json.dumps({'type': 'error', 'content': str(e)}, ensure_ascii=False)}\n\n"


@app.post("/api/research")
async def research_endpoint(request: ResearchRequest):
    """Endpoint chính xử lý yêu cầu nghiên cứu thị trường"""
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Chủ đề không được để trống")

    # Trả về một StreamingResponse với media_type chuẩn của SSE
    return StreamingResponse(
        stream_agent_events(request.topic),
        media_type="text/event-stream"
    )


if __name__ == "__main__":
    import uvicorn

    # Chạy Server Backend tại port 8000
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)