import streamlit as st
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load model and tokenizer
@st.cache_resource
def load_model():
    model = RobertaForSequenceClassification.from_pretrained("emotion_roberta")
    tokenizer = RobertaTokenizer.from_pretrained("emotion_roberta")
    return model, tokenizer

model, tokenizer = load_model()
model.eval()

EMOTIONS = ['Admiration', 'Amusement', 'Anger', 'Annoyance', 'Approval', 
            'Caring', 'Confusion', 'Curiosity', 'Desire', 'Disappointment',
            'Disapproval', 'Disgust', 'Embarrassment', 'Excitement', 'Fear', 
            'Gratitude', 'Grief', 'Joy', 'Love', 'Nervousness', 'Optimism', 
            'Pride', 'Realization', 'Relief', 'Remorse', 'Sadness', 
            'Surprise', 'Neutral']

# App UI
st.title("💬 EmotionSense – Detect Emotions from Text")
st.markdown("Enter a text message to detect the emotions behind it.")

user_input = st.text_area("Your Message", height=150)

if st.button("Analyze Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.sigmoid(outputs.logits).flatten().numpy()

        # Threshold for multi-label classification
        threshold = 0.5
        above_threshold = [(EMOTIONS[i], p) for i, p in enumerate(probs) if p > threshold]

        # Get top emotion in all cases
        top_idx = int(np.argmax(probs))
        top_emotion = EMOTIONS[top_idx]
        top_score = probs[top_idx]

        # Display Results
        st.subheader("🎯 Primary Emotion Detected:")
        st.success(f"{top_emotion} ({top_score:.2f} confidence)")

        # Additional emotions
        if above_threshold and top_emotion not in [e for e, _ in above_threshold]:
            above_threshold.append((top_emotion, top_score))

        if len(above_threshold) > 1:
            st.markdown("**Possible Additional Emotions:**")
            others = [f"{emotion} ({score:.2f})" for emotion, score in above_threshold if emotion != top_emotion]
            st.info(", ".join(others))

        # Visualization
        st.subheader("📊 Emotion Confidence Scores")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=probs, y=EMOTIONS, ax=ax, palette="viridis")
        ax.set_xlim(0, 1)
        ax.set_xlabel("Confidence Score")
        ax.set_ylabel("Emotions")
        st.pyplot(fig)

