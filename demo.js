async function simulateAnalysis() {
  const symptoms = symptomsInput.value.trim();
  const file = fileInput.files[0];
  
  if (!symptoms && !file) {
    alert("Please describe your symptoms or upload an image.");
    return;
  }

  // Show loading state
  analyzeBtn.classList.add("loading");
  analyzeBtn.disabled = true;
  
  // Prepare form data
  const formData = new FormData();
  if (file) formData.append("image", file);
  if (symptoms) formData.append("symptoms", symptoms);

  try {
    // Send to Flask backend
    const response = await fetch("http://localhost:5000/api/analyze", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) throw new Error("Analysis failed");
    
    const result = await response.json();
    
    // Display results
    analysisOutput.innerHTML = `<div class="analysis-result">${result.analysis}</div>`;
    diagnosisOutput.innerHTML = `
      <div class="diagnosis-result">
        <strong>Possible Conditions:</strong> ${result.diagnosis}
      </div>
      <div class="warning-text">
        <strong>Disclaimer:</strong> This is an AI-generated analysis. Consult a doctor for accurate diagnosis.
      </div>
    `;
    
    analysisOutput.classList.add("has-content");
    diagnosisOutput.classList.add("has-content");
  } catch (error) {
    alert("Error: " + error.message);
  } finally {
    analyzeBtn.classList.remove("loading");
    analyzeBtn.disabled = false;
  }
}
