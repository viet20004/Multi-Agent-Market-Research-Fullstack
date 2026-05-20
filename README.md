# 🤖 AI Market Research Agent - Hệ Thống Đa Tác Vụ Nghiên Cứu Thị Trường

![Độ hoàn thiện](https://img.shields.io/badge/Status-Completed-success)
![Công nghệ Backend](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python-blue)
![Công nghệ Frontend](https://img.shields.io/badge/Frontend-Next.js%20%7C%20React-black)
![AI Model](https://img.shields.io/badge/LLM-Llama%203.3%20(Groq)-orange)

## 📖 Giới thiệu
Đây là một hệ thống **Multi-Agent AI Fullstack** tự động hóa hoàn toàn quy trình nghiên cứu thị trường. Người dùng chỉ cần nhập một chủ đề (ví dụ: *"Thị phần xe điện Việt Nam 2026"*), hệ thống sẽ tự động tìm kiếm dữ liệu thực tế trên Internet, phân tích thông tin và tổng hợp thành một bản báo cáo chuyên sâu.

Dự án áp dụng kiến trúc đa tác vụ (Multi-Agent), luồng dữ liệu thời gian thực (SSE) và hỗ trợ xuất báo cáo ra các định dạng chuẩn văn phòng.

## ✨ Tính năng nổi bật
* **Kiến trúc Multi-Agent phối hợp nhịp nhàng:**
  * 🕵️ **Researcher Agent:** Tự động tìm kiếm dữ liệu thực tế và mới nhất từ Internet qua Tavily API.
  * 🧠 **Analyst Agent:** Đọc hiểu, lọc nhiễu và đúc kết các điểm dữ liệu quan trọng nhất.
  * ✍️ **Writer Agent:** Trình bày và định dạng báo cáo hoàn chỉnh dưới dạng Markdown chuyên nghiệp.
* **Luồng Stream Thời Gian Thực (SSE):** Hiển thị ngay lập tức tiến trình và logs của các Agent theo thời gian thực (giống ChatGPT) mà không cần chờ tải lại trang.
* **Tốc độ phản hồi cực nhanh:** Tích hợp mô hình Llama 3.3 thông qua Groq API cho tốc độ xử lý vượt trội.
* **Enterprise-Ready:** Hỗ trợ tính năng xuất báo cáo trực tiếp ra định dạng **PDF** (không vỡ font Tiếng Việt) và **Microsoft Word** (.doc).

## 🛠 Công nghệ sử dụng
### Backend
* **Python & FastAPI:** Khởi tạo API Server với hiệu suất cao và xử lý bất đồng bộ.
* **LangGraph / LangChain:** Xây dựng state-machine cho hệ thống Multi-Agent.
* **Groq API & Tavily Search:** LLM engine và Search engine chuyên dụng cho AI.

### Frontend
* **Next.js (App Router):** Framework React hiện đại nhất.
* **Tailwind CSS & Lucide React:** Xây dựng giao diện UI/UX trực quan, responsive.
* **React Markdown:** Render báo cáo với định dạng chuẩn.

## 🚀 Hướng dẫn cài đặt (Chạy Local)

### 1. Cài đặt Backend
```bash
# Clone dự án về máy
git clone <URL_REPO_CỦA_BẠN>

# Di chuyển vào thư mục gốc và kích hoạt môi trường ảo
python -m venv .venv
source .venv/Scripts/activate # (Trên Windows)

# Cài đặt thư viện
pip install -r requirements.txt

# Tạo file .env và thêm API Keys (GROQ_API_KEY, TAVILY_API_KEY)
# Khởi chạy Backend (Port 8000)
python api.py
