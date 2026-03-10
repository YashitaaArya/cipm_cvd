// --- MULTI-STEP FORM LOGIC ---
function nextStep(currentStep) {
    const currentStepDiv = document.getElementById(`step${currentStep}`);
    const inputs = currentStepDiv.querySelectorAll('input[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.checkValidity()) {
            input.reportValidity(); 
            isValid = false;
        }
    });

    if (!isValid) return; 

    document.getElementById(`step${currentStep}`).classList.remove('active');
    document.getElementById(`step${currentStep + 1}`).classList.add('active');
    document.getElementById(`step${currentStep}-indicator`).classList.remove('active');
    document.getElementById(`step${currentStep + 1}-indicator`).classList.add('active');
}

function prevStep(currentStep) {
    document.getElementById(`step${currentStep}`).classList.remove('active');
    document.getElementById(`step${currentStep - 1}`).classList.add('active');
    document.getElementById(`step${currentStep}-indicator`).classList.remove('active');
    document.getElementById(`step${currentStep - 1}-indicator`).classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const smokerSelect = document.getElementById('smokerSelect');
    const cigsInput = document.getElementById('cigsInput');

    if (form) {
        form.addEventListener('submit', () => {
            if(loadingOverlay) loadingOverlay.classList.remove('hidden');
        });
    }

    if (smokerSelect && cigsInput) {
        const handleSmokerChange = () => {
            if (smokerSelect.value === "0") {
                cigsInput.value = 0;
                cigsInput.readOnly = true;
                cigsInput.style.backgroundColor = "#e2e8f0";
            } else {
                cigsInput.readOnly = false;
                cigsInput.style.backgroundColor = "#fcfcfc";
                if(cigsInput.value == 0) cigsInput.value = ""; 
            }
        };
        smokerSelect.addEventListener('change', handleSmokerChange);
        handleSmokerChange(); 
    }
});