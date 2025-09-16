import streamlit as st

st.set_page_config(layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scrollytelling Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #F4F4F4;
      color: #333;
    }
    .scrolly-container {
      position: relative;
      max-width: 1000px;
      margin: 0 auto;
    }
    .sticky-visuals {
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1;
      background: white;
    }
    .visual-frame {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      transition: opacity 0.5s ease-in-out;
    }
    .visual-frame.active {
      opacity: 1;
    }
    .scrolling-text {
      position: relative;
      z-index: 2;
    }
    .step {
      min-height: 100vh;
      padding: 10% 20px;
      box-sizing: border-box;
      font-size: 1.2em;
      line-height: 1.6;
      text-align: center;
      background: linear-gradient(to bottom, transparent, rgba(244, 244, 244, 0.8) 20%, rgba(244, 244, 244, 0.95) 80%, transparent);
    }
    .step h2 {
      font-size: 2em;
      margin-bottom: 0.5em;
    }
  </style>
</head>
<body>
  <div class="scrolly-container">
    <div class="sticky-visuals">
      <div id="vis-1" class="visual-frame active">
        <iframe src="https://public.flourish.studio/visualisation/24728120/" frameborder="0" loading="lazy" style="width:100%;height:100%;"></iframe>
      </div>
      <div id="vis-2" class="visual-frame">
        <iframe src="https://public.flourish.studio/visualisation/24838022/" frameborder="0" loading="lazy" style="width:100%;height:100%;"></iframe>
      </div>
      <div id="vis-3" class="visual-frame">
        <iframe src="https://public.flourish.studio/visualisation/24838425/" frameborder="0" loading="lazy" style="width:100%;height:100%;"></iframe>
      </div>
    </div>
    <div class="scrolling-text">
      <div class="step" data-target="vis-1">
        <h2>Exposure pollution</h2>
        <p>Exposure to PM2 varies across the continent</p>
      </div>
      <div class="step" data-target="vis-2">
        <h2>Household pollution</h2>
        <p>Indoor air pollution death rates are high in the West, Central and East.</p>
      </div>
      <div class="step" data-target="vis-3">
        <h2>Ambient pollution</h2>
        <p>Northern and Southern Africa record the highest outdoor air pollution death rates</p>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const steps = document.querySelectorAll('.step');
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          const targetId = entry.target.getAttribute('data-target');
          const visual = document.getElementById(targetId);
          if (entry.isIntersecting) {
            document.querySelectorAll('.visual-frame').forEach(frame => {
              frame.classList.remove('active');
            });
            if (visual) {
              visual.classList.add('active');
            }
          }
        });
      }, { threshold: 0.5 });

      steps.forEach(step => observer.observe(step));
    });
  </script>
</body>
</html>
"""

# Très important : mettre un height assez grand pour permettre le scroll
st.components.v1.html(html_code, height=3000, scrolling=True)
