import streamlit as st

html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Enhanced Scrollytelling Experience</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', sans-serif;
      margin: 0; 
      padding: 0;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #1a1a1a;
      overflow-x: hidden;
      line-height: 1.6;
    }

    #scrolly__section {
      position: relative;
      width: 100%;
      min-height: 100vh;
    }

    .scrolly__chart {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
      background: #f8fafc;
      transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .chart-overlay {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      border-radius: 20px;
      padding: 3rem;
      max-width: 600px;
      text-align: center;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      opacity: 0;
      transform: translate(-50%, -50%) translateY(50px);
      transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      z-index: 10;
    }

    .chart-overlay.active {
      opacity: 1;
      transform: translate(-50%, -50%) translateY(0px);
    }

    .chart-title {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 1rem;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .chart-subtitle {
      font-size: 1.2rem;
      color: #64748b;
      margin-bottom: 2rem;
    }

    .chart-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }

    .stat-item {
      text-align: center;
      padding: 1rem;
      background: rgba(102, 126, 234, 0.1);
      border-radius: 12px;
      border: 1px solid rgba(102, 126, 234, 0.2);
    }

    .stat-number {
      font-size: 2rem;
      font-weight: 700;
      color: #667eea;
      display: block;
    }

    .stat-label {
      font-size: 0.9rem;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    iframe {
      width: 100%;
      height: 100%;
      border: none;
      opacity: 0.3;
      transition: opacity 0.6s ease;
    }

    .scrolly__content {
      position: relative;
      width: 100%;
      max-width: 500px;
      margin: 0 auto;
      padding: 50vh 2rem 50vh 2rem;
      z-index: 5;
    }

    .step {
      margin-bottom: 100vh;
      padding: 2.5rem;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      border-radius: 20px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      transform: translateY(50px);
      opacity: 0.7;
    }

    .step.is-active {
      transform: translateY(0px);
      opacity: 1;
      box-shadow: 0 30px 60px rgba(102, 126, 234, 0.2);
      border-color: #667eea;
    }

    .step h3 {
      font-size: 2rem;
      font-weight: 600;
      margin-bottom: 1rem;
      color: #1a1a1a;
    }

    .step p {
      font-size: 1.1rem;
      color: #4a5568;
      margin-bottom: 1.5rem;
    }

    .step-number {
      display: inline-block;
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      border-radius: 50%;
      text-align: center;
      line-height: 40px;
      font-weight: 600;
      margin-bottom: 1rem;
      font-size: 1.2rem;
    }

    .step-highlight {
      background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
      padding: 1.5rem;
      border-radius: 12px;
      border-left: 4px solid #667eea;
      margin: 1.5rem 0;
    }

    .progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 4px;
      background: linear-gradient(90deg, #667eea, #764ba2);
      z-index: 100;
      transition: width 0.3s ease;
    }

    /* Responsive design */
    @media (max-width: 768px) {
      .chart-overlay {
        margin: 1rem;
        padding: 2rem;
        max-width: calc(100vw - 2rem);
      }
      
      .chart-title {
        font-size: 1.8rem;
      }
      
      .scrolly__content {
        max-width: 100%;
        padding: 25vh 1rem 25vh 1rem;
      }
      
      .step {
        padding: 2rem;
      }
      
      .step h3 {
        font-size: 1.5rem;
      }
    }

    /* Animation keyframes */
    @keyframes slideInUp {
      from {
        opacity: 0;
        transform: translateY(50px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes pulse {
      0%, 100% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.05);
      }
    }

    .step.is-active .step-number {
      animation: pulse 2s infinite;
    }
  </style>
</head>
<body>

<div class="progress-bar" id="progress-bar"></div>

<div id="scrolly__section">
  
  <div class="scrolly__chart">
    <iframe id="flourish-iframe" src="https://flo.uri.sh/story/872914/embed#slide-0" scrolling="no"></iframe>
    
    <div class="chart-overlay" id="chart-overlay-0">
      <div class="chart-title">Data Story Begins</div>
      <div class="chart-subtitle">Explore the journey through interactive visualizations</div>
      <div class="chart-stats">
        <div class="stat-item">
          <span class="stat-number">4</span>
          <span class="stat-label">Chapters</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">∞</span>
          <span class="stat-label">Insights</span>
        </div>
      </div>
    </div>

    <div class="chart-overlay" id="chart-overlay-1">
      <div class="chart-title">Growth Trends</div>
      <div class="chart-subtitle">Examining patterns in our data</div>
      <div class="chart-stats">
        <div class="stat-item">
          <span class="stat-number">+25%</span>
          <span class="stat-label">Growth</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">142</span>
          <span class="stat-label">Data Points</span>
        </div>
      </div>
    </div>

    <div class="chart-overlay" id="chart-overlay-2">
      <div class="chart-title">Key Insights</div>
      <div class="chart-subtitle">Understanding the deeper patterns</div>
      <div class="chart-stats">
        <div class="stat-item">
          <span class="stat-number">3</span>
          <span class="stat-label">Categories</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">87%</span>
          <span class="stat-label">Accuracy</span>
        </div>
      </div>
    </div>

    <div class="chart-overlay" id="chart-overlay-3">
      <div class="chart-title">The Conclusion</div>
      <div class="chart-subtitle">What we learned from this data journey</div>
      <div class="chart-stats">
        <div class="stat-item">
          <span class="stat-number">✓</span>
          <span class="stat-label">Complete</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">∞</span>
          <span class="stat-label">Future</span>
        </div>
      </div>
    </div>
  </div>

  <div class="scrolly__content" id="scroll-content">
    
    <div class="step is-active" data-step="0">
      <div class="step-number">1</div>
      <h3>The Data Story Begins</h3>
      <p>Welcome to our interactive data journey. As you scroll through this story, watch how the visualizations transform to support each narrative point.</p>
      <div class="step-highlight">
        <strong>What you'll discover:</strong> How scrollytelling combines narrative with data visualization to create compelling stories that engage and inform.
      </div>
      <p>This first chart sets the foundation for our exploration, showing the initial dataset that sparked our investigation.</p>
    </div>

    <div class="step" data-step="1">
      <div class="step-number">2</div>
      <h3>Uncovering Growth Patterns</h3>
      <p>As we dive deeper into the data, clear growth trends begin to emerge. The visualization now highlights these patterns with enhanced clarity.</p>
      <div class="step-highlight">
        <strong>Key Finding:</strong> The data reveals a consistent 25% growth pattern across multiple categories, with peak performance occurring in Q3.
      </div>
      <p>Notice how the chart adapts to emphasize the growth trajectory, making it easier to understand the underlying trends driving these changes.</p>
    </div>

    <div class="step" data-step="2">
      <h3>Deep Dive Analysis</h3>
      <div class="step-number">3</div>
      <p>Now we're examining the data from multiple angles. The visualization transforms to show categorical breakdowns and comparative analysis.</p>
      <div class="step-highlight">
        <strong>Critical Insight:</strong> Three main categories drive 87% of the observed patterns, with remarkable consistency across different time periods.
      </div>
      <p>This perspective reveals the interconnected nature of our data points and helps explain the mechanisms behind the growth we observed earlier.</p>
    </div>

    <div class="step" data-step="3">
      <div class="step-number">4</div>
      <h3>Conclusions and Future Directions</h3>
      <p>Our data journey concludes with a comprehensive view of all findings. The final visualization synthesizes everything we've learned.</p>
      <div class="step-highlight">
        <strong>Final Takeaway:</strong> The story told by this data points to exciting possibilities for future research and strategic decision-making.
      </div>
      <p>Thank you for joining us on this scrollytelling adventure. The combination of narrative and visualization creates powerful opportunities for data communication.</p>
    </div>

  </div>

</div>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://unpkg.com/scrollama"></script>

<script>
  var scroller = scrollama();
  var currentStep = 0;

  function updateProgressBar() {
    const steps = document.querySelectorAll('.step');
    const progress = Math.min((currentStep + 1) / steps.length * 100, 100);
    document.getElementById('progress-bar').style.width = progress + '%';
  }

  function updateChartOverlay(stepIndex) {
    // Hide all overlays
    document.querySelectorAll('.chart-overlay').forEach(overlay => {
      overlay.classList.remove('active');
    });
    
    // Show current overlay with delay for smooth transition
    setTimeout(() => {
      const currentOverlay = document.getElementById(`chart-overlay-${stepIndex}`);
      if (currentOverlay) {
        currentOverlay.classList.add('active');
      }
    }, 200);

    // Update iframe opacity and source
    const iframe = document.getElementById('flourish-iframe');
    iframe.style.opacity = '0.2';
    iframe.src = `https://flo.uri.sh/story/872914/embed#slide-${stepIndex}`;
    
    // Fade iframe back in
    setTimeout(() => {
      iframe.style.opacity = '0.3';
    }, 400);
  }

  function handleResize() {
    scroller.resize();
  }

  function handleStepEnter(response) {
    // Remove active class from all steps
    d3.selectAll('.step').classed('is-active', false);
    
    // Add active class to current step
    d3.select(response.element).classed('is-active', true);

    currentStep = response.index;
    updateProgressBar();
    updateChartOverlay(currentStep);

    // Add subtle animation to the active step
    response.element.style.animation = 'slideInUp 0.8s ease-out';
    setTimeout(() => {
      response.element.style.animation = '';
    }, 800);
  }

  function handleStepExit(response) {
    // Optional: Add exit animations or effects here
  }

  function init() {
    handleResize();
    
    scroller.setup({
      step: '.step',
      offset: 0.6,
      debug: false,
      container: '#scroll-content'
    })
    .onStepEnter(handleStepEnter)
    .onStepExit(handleStepExit);

    window.addEventListener('resize', handleResize);
    
    // Initialize first overlay
    updateChartOverlay(0);
    updateProgressBar();
  }

  // Smooth scrolling for any internal links
  document.addEventListener('DOMContentLoaded', function() {
    init();
  });

  // Add some interactive hover effects
  document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.step');
    steps.forEach(step => {
      step.addEventListener('mouseenter', function() {
        if (!this.classList.contains('is-active')) {
          this.style.transform = 'translateY(-10px) scale(1.02)';
        }
      });
      
      step.addEventListener('mouseleave', function() {
        if (!this.classList.contains('is-active')) {
          this.style.transform = 'translateY(50px)';
        }
      });
    });
  });
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=3000, width = 5000, scrolling=True)
