<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>

  <h1>🎭 EmotionSense – Detect Human Emotions from Text Messages</h1>

  <p><strong>EmotionSense</strong> is a powerful and user-friendly NLP-based Streamlit web app that detects human emotions from text messages using a fine-tuned RoBERTa model. The model is trained on the GoEmotions dataset by Google and supports <strong>multi-label classification</strong> across 28 different emotion categories including <em>joy, sadness, surprise, anger, fear, neutral</em>, and many more.</p>

  <h2>🌟 Features</h2>
  <ul>
    <li>🔍 Multi-label emotion detection from any text input</li>
    <li>📊 Beautiful confidence score visualizations using Seaborn</li>
    <li>🤖 Fine-tuned RoBERTa model on the GoEmotions dataset</li>
    <li>🖥️ Interactive frontend built with Streamlit</li>
    <li>🧠 Smart fallback to the most likely emotion if none cross the threshold</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre>
emotion-sense/
├── app.py                # Main Streamlit app
├── requirements.txt      # Required dependencies
├── model drive link.txt        # Google Drive link to download the model
└── README.md             # This file
  </pre>

  <h2>🔧 Setup Instructions</h2>

  <h3>1️⃣ Clone the Repository</h3>
  <pre>
git clone https://github.com/your-username/emotion-sense.git
cd emotion-sense
  </pre>

  <h3>2️⃣ Create a Virtual Environment (Recommended)</h3>
  <pre>
python3 -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
  </pre>

  <h3>3️⃣ Install Dependencies</h3>
  <pre>
pip install -r requirements.txt
  </pre>

  <h3>4️⃣ Download the Pretrained Model</h3>
  <div class="highlight">
    <ul>
      <li>Open the <code>model_link.txt</code> file in the repo.</li>
      <li>Download the model folder named <code>emotion_roberta</code> from the Google Drive link.</li>
      <li>Place the <code>emotion_roberta</code> folder inside the <strong>root directory</strong> (same level as <code>app.py</code>).</li>
    </ul>
  </div>

  <p>📁 Final structure should look like:</p>
  <pre>
emotion-sense/
├── app.py
├── requirements.txt
├── emotion_roberta        ✅ Your downloaded model here
├── model_link.txt
└── venv
  </pre>

  <h2>🚀 Run the Streamlit App</h2>
  <pre>
streamlit run app.py
  </pre>
  <p>The app will launch in your browser at: <a href="http://localhost:8501" target="_blank">http://localhost:8501</a></p>

  <h2>🧠 Supported Emotions (28 Total)</h2>
  <p><code>Admiration</code>, <code>Amusement</code>, <code>Anger</code>, <code>Annoyance</code>, <code>Approval</code>, <code>Caring</code>, <code>Confusion</code>, <code>Curiosity</code>, <code>Desire</code>, <code>Disappointment</code>,</p>
  <p><code>Disapproval</code>, <code>Disgust</code>, <code>Embarrassment</code>, <code>Excitement</code>, <code>Fear</code>, <code>Gratitude</code>, <code>Grief</code>, <code>Joy</code>, <code>Love</code>, <code>Nervousness</code>,</p>
  <p><code>Optimism</code>, <code>Pride</code>, <code>Realization</code>, <code>Relief</code>, <code>Remorse</code>, <code>Sadness</code>, <code>Surprise</code>, <code>Neutral</code></p>

  <h2>📸 Screenshots</h2>
  <p><em>Add your own screenshot here:</em></p>
  <pre>
📷 EmotionSense UI
[Your Screenshot Here]
  </pre>

  <h2>📝 License</h2>
  <p>This project is licensed under the <a href="https://choosealicense.com/licenses/mit/" target="_blank">MIT License</a>.</p>

  <h2>🙌 Acknowledgements</h2>
  <ul>
    <li>🤗 <a href="https://huggingface.co/transformers/" target="_blank">HuggingFace Transformers</a></li>
    <li>📊 <a href="https://seaborn.pydata.org/" target="_blank">Seaborn</a></li>
    <li>🎨 <a href="https://streamlit.io/" target="_blank">Streamlit</a></li>
    <li>📚 <a href="https://github.com/google-research/google-research/tree/master/goemotions" target="_blank">GoEmotions Dataset</a></li>
  </ul>

  <h2>👨‍💻 Author</h2>
  <p>Developed with ❤️ by <strong>Arjun</strong><br/>
     GitHub: <a href="https://github.com/Arjun5804" target="_blank">https://github.com/Arjun5804</a>
  </p>

</body>
</html>

