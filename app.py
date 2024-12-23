
st.title("Dashboard Data")
data = pd.read_csv('day.csv')
st.write(data)
!streamlit run app.py &
public_url = ngrok.connect(port=8501)
print(f"Public URL: {public_url}")
