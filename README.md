# OpenOA: Wind Plant Analysis Platform (Wrapper)

### Live Demo
**[Click Here to Launch App](https://openoa-fldnqvn7b4u5mbeaya3kfk.streamlit.app/)**

### Project Overview
This project wraps the NREL `OpenOA` library into a deployable **Full Stack Application**.

Since `OpenOA` is a library and not a web server, I architected a microservices solution:
1. **Backend:** Exposes OpenOA functionality via REST API endpoints.
2. **Frontend:** A user-friendly dashboard for wind plant analysis.
3. **Deployment:** Dockerized and deployed on Render and Streamlit Cloud.

### Tech Stack
* **Language:** Python 3.10
* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit
* **Core Library:** OpenOA
* **Cloud:** Render, Streamlit Cloud

### How to Run Locally
```bash
# 1. Clone the repo
git clone [https://github.com/YOUR_USERNAME/OpenOA.git](https://github.com/YOUR_USERNAME/OpenOA.git)
cd OpenOA

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Backend
uvicorn main:app --reload

# 4. Run Frontend (in a new terminal)
streamlit run frontend.py