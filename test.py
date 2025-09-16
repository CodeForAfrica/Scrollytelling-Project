import streamlit as st

st.set_page_config(layout="wide")


html_code = """
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Scrollytelling - Flourish embed</title>
<style>
  :root { --accent: #104E8B; --active: goldenrod; }
  body { margin:0; font-family: Poppins, Arial, sans-serif; background:#f7f7f7; color:#222; }
  .scrolly-container { max-width:1200px; margin:0 auto; padding:24px; }
  .scrolly-inner { display:flex; gap:24px; align-items:flex-start; }

  /* Sticky visuals (single iframe) */
  .visuals {
    position: sticky;
    top: 20px;              /* distance from top of iframe viewport */
    flex: 1 1 60%;
    height: calc(100vh - 40px);
    background: white;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    border-radius: 6px;
    overflow: hidden;
  }
  .visuals iframe {
    width:100%;
    height:100%;
    border:0;
    display:block;
    background: transparent;
  }

  /* Scrolling text column */
  .textcol {
    flex: 0 0 35%;
    max-width: 35%;
  }
  .step {
    box-sizing: border-box;
    margin-bottom: 24px;
    padding: 28px;
    border: 2px solid var(--accent);
    border-radius: 8px;
    background: rgba(255,255,255,0.95);
    transition: transform 0.28s ease, background-color 0.28s ease;
  }
  .step.is-active {
    border-color: var(--active);
    background: rgba(255, 237, 179, 0.95);
    transform: translateY(-6px);
  }

  /* make sure steps are readable on narrow screens */
  @media (max-width: 900px) {
    .scrolly-inner { flex-direction: column; }
    .visuals { position: relative; height: 360px; width: 100%; top: 0; }
    .textcol { max-width: 100%; width:100%; }
  }
</style>
</head>
<body>
  <div class="scrolly-container">
    <h2>Scrollytelling - example</h2>
    <div class="scrolly-inner">
      <!-- left: scrolling steps -->
      <div class="textcol">
        <!-- NOTE: replace data-src values with your embed URLs (embed path) -->
        <div class="step" data-src="https://flo.uri.sh/visualisation/24728120/embed">
          <h3>Exposure pollution</h3>
          <p>Exposure to PM2 varies across the continent.</p>
        </div>

        <div class="step" data-src="https://flo.uri.sh/visualisation/24838022/embed">
          <h3>Household pollution</h3>
          <p>Indoor air pollution death rates are high in the West, Central and East.</p>
        </div>

        <div class="step" data-src="https://flo.uri.sh/visualisation/24838425/embed">
          <h3>Ambient pollution</h3>
          <p>Northern and Southern Africa record the highest outdoor air pollution death rates.</p>
        </div>
      </div>

      <!-- right: single iframe that we update -->
      <div class="visuals">
        <iframe id="flourish-iframe" src="https://flo.uri.sh/visualisation/24728120/embed" scrolling="no" loading="lazy"></iframe>
      </div>
    </div>
  </div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const steps = Array.from(document.querySelectorAll('.step'));
  const iframe = document.getElementById('flourish-iframe');

  // set each step height equal to the iframe viewport height for reliable intersection
  function setStepHeights() {
    const vh = window.innerHeight;
    steps.forEach(s => s.style.minHeight = (vh) + 'px');
  }
  setStepHeights();
  window.addEventListener('resize', setStepHeights);

  // IntersectionObserver to detect which step is centered/visible
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // remove active from all and add to the currently intersecting
        steps.forEach(s => s.classList.remove('is-active'));
        entry.target.classList.add('is-active');

        // get the embed URL from data-src and update the iframe
        const src = entry.target.dataset.src;
        if (src) {
          // Only change if different (prevents reloads when same)
          if (iframe.src !== src) {
            iframe.src = src;
          }
        }
      }
    });
  }, { threshold: 0.55 }); // ~55% visible triggers

  // observe steps
  steps.forEach(s => observer.observe(s));
});
</script>
</body>
</html>
"""

# Use scrolling=True so the embedded HTML can scroll inside the Streamlit iframe.
# Height should be large enough for the embedded viewport (adjust to your needs).
st.components.v1.html(html_code, height=900, scrolling=True)
