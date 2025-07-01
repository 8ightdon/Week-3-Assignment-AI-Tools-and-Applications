# 🛠️ Mastering the AI Toolkit – AI Tools & Applications Assignment
># 🧠 End-to-End ML, DL, and NLP Project Suite  
*Iris | MNIST | Product Reviews (NER + Sentiment)*   

Welcome to our group assignment for **AI Tools and Applications**. In this project, we explore real-world applications of leading AI frameworks including TensorFlow, PyTorch, Scikit-learn, and spaCy — from classical machine learning to deep learning and natural language processing.

> 🧑‍🤝‍🧑 Group Members: Derick, Presley, Daisy, Kerama, Doreen and Berlyn

---

## 📂 Project Structure

```bash
📁 ai-toolkit-assignment/
├── Task1_Scikit_Iris.ipynb           # Classical ML with Scikit-learn
├── Task2_MNIST_CNN_TensorFlow.ipynb  # CNN for handwritten digit recognition
├── Task3_spaCy_NLP.ipynb             # NER + Sentiment with spaCy
├── app.py                            # Streamlit app for MNIST model
├── mnist_cnn.h5                      # Saved trained model
├── README.md                         # This file
└── Report_AI_Toolkit.pdf             # Theory + outputs + ethics writeup


---

## ✅ Task Breakdown

### 🌸 Task 1: Iris Classification (Scikit-learn)

- **Dataset:** Iris (150 flower samples, 4 features)
- **Algorithm:** `DecisionTreeClassifier`
- **Train-Test Split:** 80-20
- **Results:**
  - ✅ Accuracy: `100%`
  - ✅ Precision & Recall: `1.00`
- **Visual Output:** Confusion Matrix heatmap

> This classic ML task demonstrates quick classification using simple decision trees. No missing values. Model trained with reproducibility (`random_state=42`).

---

### 🔢 Task 2: MNIST Digit Recognition (TensorFlow CNN)

- **Dataset:** MNIST Handwritten Digits (60k train / 10k test)
- **Model:**
  - Input: (28x28 grayscale images)
  - 2× Conv2D + MaxPooling → Flatten → Dense + Softmax
- **Training:**
  - 5 Epochs
  - Optimizer: Adam
  - Loss: SparseCategoricalCrossentropy
- **Performance:**
  - ✅ Final Accuracy: **98.6%**
- **Visual Output:**
  - Accuracy vs Epochs Plot
  - Confusion Matrix for test predictions

> A robust CNN pipeline demonstrating deep learning for image classification.

---

### 🗣️ Task 3: NLP on Product Reviews (spaCy + Rule-Based Sentiment)

- **Dataset:** 10 synthetic Amazon-style product reviews
- **NLP Techniques Used:**
  - **Named Entity Recognition** (spaCy)
  - **Sentiment Analysis** (Keyword-based rules)
- **Entities Extracted:** `ORG`, `PERSON`, `PRODUCT`
- **Sentiment Classification:** `Positive`, `Negative`, `Neutral`
- **Visual Output:**
  - Pie chart: Sentiment distribution
  - Bar charts: Brand mentions, Entity types
  - Histogram: Sentiment score frequency

#### 📈 Result Summary:

| Metric                          | Value         |
|-------------------------------|---------------|
| Total Reviews Analyzed         | 10            |
| Entities Extracted             | 14            |
| Brands Mentioned               | 11 unique     |
| Product Entities Extracted     | 0 (due to label sparsity) |
| Sentiment Distribution         | 70% Positive, 20% Negative, 10% Neutral |
| CSV Export                     | ✅ `amazon_reviews_nlp_analysis.csv` |

> Sample Entity: `"HP"` detected as brand; Sentiment score: `-3`  
> Example Positive Review: `"Apple MacBook Air is lightweight and perfect for students."`

---

## 📊 Visual Samples

### Confusion Matrix – Iris  
![](assets/iris_confusion_matrix.png)

### Accuracy Curve – MNIST  
![](assets/mnist_accuracy.png)

### Sentiment Pie Chart – NLP  
![](assets/nlp_sentiment_pie.png)

---

## 💾 CSV Export

> File: **`amazon_reviews_nlp_analysis.csv`**

Includes:
- Review Text
- Sentiment Label & Score
- Extracted Brands & Products (if any)

Use this file for further analysis in Excel, Tableau, or BI tools.

---

## ⚙️ Setup Instructions

Run in **Google Colab** or a local Python environment.  
Install dependencies via:

```bash
pip install -q spacy textblob scikit-learn tensorflow matplotlib seaborn
python -m spacy download en_core_web_sm

To launch Streamlit (optional):
streamlit run app.py

