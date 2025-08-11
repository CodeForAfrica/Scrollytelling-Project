import streamlit as st

st.set_page_config(layout="wide")

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Scroll-driven Story - Text over Chart</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" crossorigin="anonymous" />
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0;
      padding: 0;
      background: #fff;
      color: #1d1d1d;
      overflow-x: hidden;
    }

    /* Main container - fullscreen chart with text overlay */
    #scrolly__section {
      position: relative;
      width: 100vw;
      height: 100vh;
    }

    /* Full-screen chart background */
    .scrolly__chart {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
      background: #fff;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
      transition: opacity 0.5s ease-in-out;
    }

    /* Text overlay - scrollable over the chart */
    .scrolly__content {
      position: relative;
      width: 100%;
      height: auto;
      z-index: 10;
      padding: 2rem;
      
      /* Hide scrollbar completely */
      scrollbar-width: none;
      -ms-overflow-style: none;
    }

    .scrolly__content::-webkit-scrollbar {
      display: none;
    }

    /* Text steps positioned over the chart */
    .step {
      margin: 0 0 100vh 0;
      padding: 2rem;
      max-width: 500px;
      background: rgba(255, 255, 255, 0.92);
      border: 2px solid transparent;
      border-radius: 12px;
      backdrop-filter: blur(20px) saturate(180%);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
      opacity: 0.3;
      transform: translateY(50px) scale(0.95);
      transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }

    /* Progressive positioning for text blocks */
    .step:nth-child(1) {
      margin-left: 5%;
    }
    
    .step:nth-child(2) {
      margin-left: 60%;
    }
    
    .step:nth-child(3) {
      margin-left: 20%;
    }
    
    .step:nth-child(4) {
      margin-left: 70%;
    }

    /* Active step styling */
    .step.is-active {
      opacity: 1;
      transform: translateY(0) scale(1);
      border-color: #104E8B;
      background: rgba(255, 255, 255, 0.95);
      box-shadow: 0 12px 48px rgba(16, 78, 139, 0.2);
    }

    .step h3 {
      font-size: 1.8rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #104E8B;
      transition: color 0.4s ease;
    }

    .step.is-active h3 {
      color: #D4AF37;
    }

    .step p {
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 1rem;
      color: #2c2c2c;
    }

    .step .highlight {
      background: linear-gradient(120deg, #D4AF37 0%, #F4E87C 100%);
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 600;
      color: #2c2c2c;
    }

    /* Progress indicator */
    .progress-indicator {
      position: fixed;
      right: 2rem;
      top: 50%;
      transform: translateY(-50%);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .progress-dot {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(16, 78, 139, 0.3);
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }

    .progress-dot::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: transparent;
      transition: all 0.4s ease;
    }

    .progress-dot.active {
      background: #D4AF37;
      transform: scale(1.3);
      box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);
    }

    .progress-dot.active::after {
      background: #fff;
    }

    /* Chart elements animation control */
    .chart-element {
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .chart-element.animate-in {
      opacity: 1;
      transform: translateY(0);
    }

    /* Responsive design */
    @media (max-width: 768px) {
      .step {
        max-width: 90%;
        margin-left: 5% !important;
        margin-right: 5%;
        padding: 1.5rem;
      }
      
      .progress-indicator {
        bottom: 2rem;
        top: auto;
        right: 50%;
        transform: translateX(50%);
        flex-direction: row;
      }

      .step h3 {
        font-size: 1.5rem;
      }

      .step p {
        font-size: 1rem;
      }
    }

    /* Header styling */
    .app-header {
      background: linear-gradient(135deg, #104E8B 0%, #1e5f9e 100%);
      color: white;
      text-align: center;
      padding: 3rem 1rem;
      position: relative;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(16, 78, 139, 0.3);
    }

    .app-header h1 {
      font-weight: 800;
      font-size: 3.2rem;
      margin-bottom: 0.5rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .app-header h2 {
      font-weight: 300;
      font-size: 1.3rem;
      opacity: 0.9;
      margin-bottom: 2rem;
    }

    .app-header .intro-text {
      font-size: 1.1rem;
      max-width: 600px;
      margin: 0 auto;
      opacity: 0.85;
      line-height: 1.6;
    }

    /* Smooth scrolling */
    html {
      scroll-behavior: smooth;
    }
  </style>
</head>
<body>

  <header class="app-header">
    <div class="container">
      <h1>Data Scrollytelling</h1>
      <h2>Interactive Visualization Journey</h2>
      <p class="intro-text">Scroll through the story as data elements reveal themselves progressively with each narrative step.</p>
    </div>
  </header>

  <!-- Progress indicator -->
  <div class="progress-indicator" id="progress-indicators">
    <div class="progress-dot active" data-step="0" title="Premature Deaths"></div>
    <div class="progress-dot" data-step="1" title="Children Impact"></div>
    <div class="progress-dot" data-step="2" title="Regional Analysis"></div>
    <div class="progress-dot" data-step="3" title="Solutions"></div>
  </div>

  <div id="scrolly__section">
    
    <!-- Full-screen chart background -->
    <div class="scrolly__chart">
      <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
    </div>

    <!-- Text content overlaid on chart -->
    <div class="scrolly__content" id="scroll-content">
      
      <div class="step is-active" data-step="0" data-chart-elements="global-deaths,mortality-rate">
        <h3>🌍 Global Health Crisis</h3>
        <p><span class="highlight">89% of premature deaths</span> from air pollution occurred in low- and middle-income countries.</p>
        <p>This stark disparity reveals how environmental health challenges disproportionately affect the world's most vulnerable populations.</p>
      </div>

      <div class="step" data-step="1" data-chart-elements="child-mortality,age-groups">
        <h3>👶 Children at Risk</h3>
        <p>Over <span class="highlight">237,000 deaths of children</span> under age 5 are attributed to air pollution annually.</p>
        <p>Young lungs are particularly susceptible to environmental toxins, making children our most vulnerable population in the fight for clean air.</p>
      </div>

      <div class="step" data-step="2" data-chart-elements="regional-data,pollution-levels">
        <h3>📊 Regional Variations</h3>
        <p>Air quality and health outcomes vary dramatically across regions, with <span class="highlight">developing nations</span> bearing the heaviest burden.</p>
        <p>Understanding these geographical patterns is crucial for targeted interventions and resource allocation.</p>
      </div>

      <div class="step" data-step="3" data-chart-elements="solutions,trends">
        <h3>💡 Path Forward</h3>
        <p>Data-driven policies and <span class="highlight">targeted interventions</span> can significantly reduce air pollution mortality.</p>
        <p>The evidence points to clear priorities: invest in clean energy, improve monitoring systems, and protect vulnerable communities.</p>
      </div>

    </div>
  </div>

  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script src="https://unpkg.com/scrollama"></script>

  <script>
    let scroller = scrollama();
    let currentSlide = 0;

    // Animation sequences for chart elements
    const chartAnimations = {
      0: () => animateChartElements(['global-deaths', 'mortality-rate']),
      1: () => animateChartElements(['child-mortality', 'age-groups']),
      2: () => animateChartElements(['regional-data', 'pollution-levels']),
      3: () => animateChartElements(['solutions', 'trends'])
    };

    function animateChartElements(elements) {
      // This function would communicate with your Flourish chart
      // to progressively reveal specific elements
      console.log('Animating chart elements:', elements);
      
      // Send message to iframe to trigger specific animations
      const iframe = document.getElementById('flourish-iframe');
      if (iframe.contentWindow) {
        iframe.contentWindow.postMessage({
          type: 'animate-elements',
          elements: elements
        }, '*');
      }
    }

    function updateChart(slideNum) {
      if (slideNum !== currentSlide) {
        const iframe = document.getElementById('flourish-iframe');
        
        // Smooth transition effect
        iframe.style.opacity = '0.8';
        
        setTimeout(() => {
          iframe.src = `https://flo.uri.sh/story/872914/embed#slide-${slideNum}`;
          
          // Trigger progressive animation after chart loads
          setTimeout(() => {
            if (chartAnimations[slideNum]) {
              chartAnimations[slideNum]();
            }
            iframe.style.opacity = '1';
          }, 300);
          
        }, 200);
        
        currentSlide = slideNum;
      }
    }

    function updateProgressIndicator(activeIndex) {
      d3.selectAll('.progress-dot')
        .classed('active', false);
      d3.select(`.progress-dot[data-step="${activeIndex}"]`)
        .classed('active', true);
    }

    function handleStepEnter(response) {
      // Update active step
      d3.selectAll('.step').classed('is-active', false);
      d3.select(response.element).classed('is-active', true);

      const slideNum = response.index;
      updateChart(slideNum);
      updateProgressIndicator(slideNum);
    }

    function scrollToStep(stepIndex) {
      const targetStep = document.querySelector(`.step[data-step="${stepIndex}"]`);
      if (targetStep) {
        targetStep.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    }

    function handleResize() {
      scroller.resize();
    }

    function init() {
      // Setup scrollama with optimized settings
      scroller.setup({
        step: '.step',
        offset: 0.5, // Trigger when step is centered
        debug: false,
      })
      .onStepEnter(handleStepEnter);

      // Progress indicator click handlers
      d3.selectAll('.progress-dot')
        .on('click', function() {
          const stepIndex = parseInt(d3.select(this).attr('data-step'));
          scrollToStep(stepIndex);
        });

      // Keyboard navigation
      document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === ' ') {
          e.preventDefault();
          if (currentSlide < 3) scrollToStep(currentSlide + 1);
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (currentSlide > 0) scrollToStep(currentSlide - 1);
        }
      });

      // Handle window resize
      window.addEventListener('resize', handleResize);

      // Smooth scroll behavior
      document.addEventListener('wheel', function(e) {
        e.preventDefault();
        const delta = e.deltaY;
        window.scrollBy({
          top: delta * 0.8,
          behavior: 'smooth'
        });
      }, { passive: false });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }

    // Listen for messages from Flourish iframe (if supported)
    window.addEventListener('message', function(event) {
      if (event.data.type === 'flourish-ready') {
        console.log('Flourish chart is ready for animations');
      }
    });

  </script>

</body>
</html>
"""

# Render the HTML in Streamlit
st.components.v1.html(html_code, height=1000, width=4000, scrolling=True)
