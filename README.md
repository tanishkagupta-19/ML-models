<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Machine Learning Models Collection — Tanishka Gupta</title>
  <style>
    :root{
      --bg:#0b0f1a; --panel:#111826; --muted:#90a4b4; --text:#e5eef7; --accent:#7aa2ff; --card:#0f172a; --code:#0a1220; --border:#1f2a44;
    }
    html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:Inter,system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.6}
    a{color:var(--accent);text-decoration:none} a:hover{opacity:.9;text-decoration:underline}
    .container{max-width:1000px;margin:0 auto;padding:40px 20px}
    header{background:linear-gradient(180deg,rgba(122,162,255,.15),transparent);padding:28px 24px;border:1px solid var(--border);border-radius:18px}
    h1{margin:0 0 8px;font-size: clamp(28px, 4vw, 40px)}
    .subtitle{color:var(--muted);font-size:clamp(14px,2.2vw,16px);margin-top:6px}
    .badges{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
    .badge{background:var(--card);border:1px solid var(--border);padding:6px 10px;border-radius:999px;font-size:12px}
    section{margin-top:36px;background:var(--panel);border:1px solid var(--border);border-radius:16px;padding:24px}
    h2{margin-top:0;font-size:clamp(20px,3vw,26px)}
    h3{margin-top:18px;font-size:clamp(16px,2.5vw,20px)}
    .grid{display:grid;gap:14px}
    .two{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
    pre{background:var(--code);padding:16px;border-radius:12px;overflow:auto;border:1px solid var(--border)}
    code{font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px}
    ul{margin:0 0 0 18px}
    .kbd{font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#0c1426;border:1px solid var(--border);padding:2px 6px;border-radius:6px}
    footer{color:var(--muted);margin:28px 2px}
    .toc a{display:block;margin:6px 0}
    .pill{display:inline-block;background:#0c1426;border:1px solid var(--border);padding:2px 8px;border-radius:999px;font-size:12px;color:var(--muted)}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🤖 Machine Learning Models Collection</h1>
      <p class="subtitle">A curated portfolio of end-to-end ML projects — data prep, EDA, model training, evaluation, persistence, and deployment.</p>
      <div class="badges">
        <span class="badge">Python</span>
        <span class="badge">scikit-learn</span>
        <span class="badge">Pandas</span>
        <span class="badge">Matplotlib</span>
        <span class="badge">NLP / TF-IDF</span>
        <span class="badge">Streamlit</span>
        <span class="badge">joblib</span>
      </div>
      <p style="margin-top:16px;">
        <a href="https://github.com/tanishkagupta-19/ML-Models" target="_blank">
          <img src="https://img.shields.io/badge/GitHub-Repo-black?logo=github" alt="GitHub Repo">
        </a>
        <a href="https://ml-models-tanishkagupta-19.streamlit.app/" target="_blank">
          <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit App">
        </a>
      </p>
    </header>

    <section class="toc">
      <h2>Contents</h2>
      <a href="#structure">Repository Structure</a>
      <a href="#projects">Projects Overview</a>
      <a href="#stack">Tech Stack</a>
      <a href="#run">Getting Started</a>
      <a href="#results">Results Snapshot</a>
      <a href="#future">Future Enhancements</a>
      <a href="#author">Author</a>
    </section>

    <section id="structure">
      <h2>📂 Repository Structure</h2>
      <pre><code>├── Decision_Trees/
│   ├── CreditRiskDetector.joblib
│   ├── CreditRiskDetector_app.py
│   ├── credit_risk_dataset.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Linear_Regression/
│   ├── HousePricePrediction.joblib
│   ├── HousePricePrediction_app.py
│   ├── USA_Housing.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Logistic_Regression/
│   ├── employeeChurnModel.joblib
│   ├── employeeChurn_app.py
│   ├── HR_comma_sep.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Random_Forest/
│   ├── CreditRiskDetector_RF.joblib
│   ├── CreditRiskDetector_RF_app.py
│   ├── DfvsRF.ipynb
│   ├── credit_risk_dataset.csv
│   └── requirements.txt
│
├── SVM/
│   ├── EmailSpamDetection.joblib
│   ├── EmailSpamDetection_app.py
│   ├── spam.csv
│   ├── tfidf_vectorizer.joblib
│   ├── model.ipynb
│   └── requirements.txt</code></pre>
    </section>

    <section id="projects">
      <h2>📝 Projects Overview</h2>

      <h3>1) House Price Prediction <span class="pill">Linear Regression</span></h3>
      <ul>
        <li><strong>Goal:</strong> Predict housing prices using features such as area, bedrooms, bathrooms, and year built.</li>
        <li><strong>Dataset:</strong> <code>USA_Housing.csv</code></li>
        <li><strong>Artifacts:</strong> <code>HousePricePrediction.joblib</code>, <code>HousePricePrediction_app.py</code>, <code>model.ipynb</code></li>
      </ul>

      <h3>2) Credit Risk Detection <span class="pill">Decision Tree</span> <span class="pill">Random Forest</span></h3>
      <ul>
        <li><strong>Goal:</strong> Predict loan default risk based on applicant demographics and financials.</li>
        <li><strong>Dataset:</strong> <code>credit_risk_dataset.csv</code></li>
        <li><strong>Artifacts (DT):</strong> <code>CreditRiskDetector.joblib</code>, <code>CreditRiskDetector_app.py</code></li>
        <li><strong>Artifacts (RF):</strong> <code>CreditRiskDetector_RF.joblib</code>, <code>CreditRiskDetector_RF_app.py</code>, <code>DfvsRF.ipynb</code></li>
      </ul>

      <h3>3) Employee Churn Prediction <span class="pill">Logistic Regression</span></h3>
      <ul>
        <li><strong>Goal:</strong> Predict whether an employee will leave the company.</li>
        <li><strong>Dataset:</strong> <code>HR_comma_sep.csv</code></li>
        <li><strong>Artifacts:</strong> <code>employeeChurnModel.joblib</code>, <code>employeeChurn_app.py</code>, <code>model.ipynb</code></li>
      </ul>

      <h3>4) Email Spam Detection <span class="pill">SVM</span> <span class="pill">NLP</span></h3>
      <ul>
        <li><strong>Goal:</strong> Classify emails as <em>Spam</em> or <em>Not Spam</em>.</li>
        <li><strong>Techniques:</strong> Text cleaning, TF-IDF vectorization.</li>
        <li><strong>Dataset:</strong> <code>spam.csv</code></li>
        <li><strong>Artifacts:</strong> <code>EmailSpamDetection.joblib</code>, <code>tfidf_vectorizer.joblib</code>, <code>EmailSpamDetection_app.py</code>, <code>model.ipynb</code></li>
      </ul>
    </section>

    <section id="stack">
      <h2>🛠️ Tech Stack</h2>
      <div class="grid two">
        <div>
          <h3>Core</h3>
          <ul>
            <li>Python</li>
            <li>NumPy, Pandas</li>
            <li>scikit-learn</li>
            <li>Matplotlib, Seaborn</li>
          </ul>
        </div>
        <div>
          <h3>NLP & Deployment</h3>
          <ul>
            <li>NLTK, TF-IDF (Spam)</li>
            <li>Streamlit apps</li>
            <li>Model persistence with <code>joblib</code></li>
          </ul>
        </div>
      </div>
    </section>

    <section id="run">
      <h2>▶️ Getting Started</h2>
      <ol>
        <li>
          <p><strong>Clone the repository</strong></p>
          <pre><code>git clone https://github.com/tanishkagupta-19/ML-Models.git
cd ML-Models</code></pre>
        </li>
        <li>
          <p><strong>Navigate into a project</strong> (example: Linear Regression)</p>
          <pre><code>cd Linear_Regression</code></pre>
        </li>
        <li>
          <p><strong>Install dependencies</strong></p>
          <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>
          <p><strong>Run the app</strong></p>
          <pre><code>streamlit run HousePricePrediction_app.py</code></pre>
        </li>
      </ol>
      <p>Tip: Use <span class="kbd">python -m venv .venv</span> and <span class="kbd">.venv\\Scripts\\activate</span> (Windows) or <span class="kbd">source .venv/bin/activate</span> (macOS/Linux) to keep environments isolated.</p>
    </section>

    <section id="results">
      <h2>📈 Results Snapshot</h2>
      <ul>
        <li><strong>House Price Prediction:</strong> R² ≈ 0.90 (Random Forest baseline comparison)</li>
        <li><strong>Credit Risk Prediction:</strong> Recall improved by ~15% with Random Forest vs. baseline</li>
        <li><strong>Employee Churn:</strong> Accuracy ≈ 82% with Logistic Regression</li>
        <li><strong>Email Spam Detection:</strong> Accuracy ≈ 96% with SVM</li>
      </ul>
      <p class="subtitle">Note: Metrics are indicative; see notebooks for exact runs and evaluation details.</p>
    </section>

    <section id="future">
      <h2>📌 Future Enhancements</h2>
      <ul>
        <li>Live demos via Streamlit Cloud / Hugging Face Spaces</li>
        <li>Unified dashboard to compare models across tasks</li>
        <li>Additional deep learning experiments (LSTM/CNN)</li>
      </ul>
    </section>

    <section id="author">
      <h2>👩‍💻 Author</h2>
      <p><strong>Tanishka Gupta</strong></p>
      <p>
        <a href="https://www.linkedin.com/in/tanishkagupta19" target="_blank" rel="noopener">LinkedIn</a>
        &nbsp;•&nbsp;
        <a href="https://github.com/tanishkagupta-19" target="_blank" rel="noopener">GitHub</a>
      </p>
    </section>

    <footer>
      <p>© <span id="year"></span> Tanishka Gupta — ML Models.</p>
    </footer>
  </div>
  <script>document.getElementById('year').textContent=new Date().getFullYear()</script>
</body>
</html>
