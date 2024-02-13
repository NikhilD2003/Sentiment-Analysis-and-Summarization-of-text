# Sentiment-Analysis-and-Summarization-of-text-in-different-languages
# Description
This project aims to develop a system for sentiment analysis and text summarization. Sentiment analysis involves classifying the emotional tone of a piece of text as positive, negative, or neutral. Text summarization, on the other hand, involves condensing the main ideas of a document into a concise form. The goal is to create a tool that can efficiently analyze sentiments and provide meaningful summaries of text.
# Methodology
![Screenshot 2024-01-31 214826](https://github.com/NikhilD2003/Sentiment-Analysis-and-Summarization-of-text/assets/150776453/f311770d-4b24-4cab-adc5-d85c4e711dd6)
# Steps to run the code
Install Required Packages:
Open a terminal and run the following command to install the necessary Python packages:

bash
Copy code
pip install Flask textblob bert-extractive-summarizer
Create Project Structure:
Create the project structure as mentioned earlier:

arduino
Copy code
/multilingual_sentiment_analysis
├── app.py
├── templates
│   ├── index.html
└── static
    ├── styles.css
Copy Code:
Copy the respective code into the appropriate files:

Copy the content of app.py into a file named app.py in the project root.
Copy the content of index.html into a file named index.html inside the templates folder.
Copy the content of styles.css into a file named styles.css inside the static folder.
Run the Application:
In the terminal, navigate to the project's root directory (where app.py is located) and run the following command:

bash
Copy code
python app.py
This will start the Flask development server. You should see output indicating that the server is running. By default, it will run on http://127.0.0.1:5000/.

Access the Application:
Open your web browser and navigate to the following address:

arduino
Copy code
http://127.0.0.1:5000/
This will take you to the Multilingual Sentiment Analysis web application. Enter text in the provided textarea, submit the form, and view the sentiment analysis results and summary displayed on the page.

Make sure to have an active internet connection when running the code, as the bert-extractive-summarizer library might need to download additional resources for summarization.

If there are any issues or errors, please let me know, and we can troubleshoot them together.
# Screenshot of webpage
![web](https://github.com/NikhilD2003/Sentiment-Analysis-and-Summarization-of-text/assets/150776453/90218fc5-e1db-4a19-b5b1-14a058f84b11)
# Screenshot of result
![result](https://github.com/NikhilD2003/Sentiment-Analysis-and-Summarization-of-text/assets/150776453/167f0cfa-f56f-406c-a3f5-f4f471ceecd6)
# Conclusion
The developed system successfully combines sentiment analysis and text summarization capabilities. The sentiment analysis model demonstrates accuracy in discerning emotional tones, while the summarization module efficiently condenses lengthy texts into concise summaries. The integration of these components provides a versatile tool for extracting insights from textual data, making it valuable for applications in various domains such as social media monitoring, news analysis, and content summarization. Further improvements and optimizations could enhance the system's performance, paving the way for broader practical applications in the field of natural language processing.
