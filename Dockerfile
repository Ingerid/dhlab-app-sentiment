FROM python:3.11-slim
EXPOSE 8501
WORKDIR /sentiment
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run st_sentiment.py  --server.baseUrlPath /sentiment
