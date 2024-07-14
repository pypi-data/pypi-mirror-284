document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (form.id === 'payment-form') {
                const paymentMethod = document.getElementById('payment-method').value;
                const requiredInputs = paymentMethod === 'credit-card' ?
                    document.querySelectorAll('#credit-card-info input') :
                    document.querySelectorAll('#paypal-info input');
                
                let isValid = true;
                requiredInputs.forEach(input => {
                    if (input.value.trim() === '') {
                        isValid = false;
                        input.style.borderColor = 'red';
                    } else {
                        input.style.borderColor = '#ccc';
                    }
                });

                if (!isValid) {
                    event.preventDefault();
                    alert('Please fill in all required fields for the selected payment method.');
                }
            }
        });
    });

    const navLinks = document.querySelectorAll('nav ul li a');
    const currentUrl = window.location.pathname;
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });

    // Toggle inputs based on search method
    const searchMethodRadios = document.getElementsByName("search-method");
    const urlInputs = document.getElementById("url-inputs");
    const nameInputs = document.getElementById("name-inputs");

    if (searchMethodRadios.length > 0) {
        searchMethodRadios.forEach(radio => {
            radio.addEventListener("change", function() {
                if (this.value === "url") {
                    urlInputs.style.display = "block";
                    nameInputs.style.display = "none";
                } else {
                    urlInputs.style.display = "none";
                    nameInputs.style.display = "block";
                }
            });
        });
    }

    // Fetch existing templates from the server
    const templateSelect = document.getElementById("select-template");
    if (templateSelect) {
        fetch("/get_templates")
            .then(response => response.json())
            .then(data => {
                data.templates.forEach(template => {
                    const option = document.createElement("option");
                    option.value = template;
                    option.text = template;
                    templateSelect.add(option);
                });
            });
    }

    // Validation for Save Template
    const templateForm = document.getElementById('template-form');
    if (templateForm) {
        templateForm.addEventListener('submit', function(event) {
            const action = event.submitter.value;
            if (action === 'Save Template') {
                const templateName = document.getElementById('template-name');
                if (templateName.value.trim() === '') {
                    templateName.style.borderColor = 'red';
                    event.preventDefault();
                    alert('Please provide a name for the template.');
                }
            }
        });
    }

    const paymentMethodSelect = document.getElementById('payment-method');
    const creditCardInfo = document.getElementById('credit-card-info');
    const paypalInfo = document.getElementById('paypal-info');

    if (paymentMethodSelect) {
        paymentMethodSelect.addEventListener('change', function() {
            const method = this.value;
            if (method === 'credit-card') {
                creditCardInfo.classList.add('active');
                paypalInfo.classList.remove('active');
            } else {
                creditCardInfo.classList.remove('active');
                paypalInfo.classList.add('active');
            }
        });
    }

    // Set initial visibility based on the selected payment method
    if (paymentMethodSelect) {
        const method = paymentMethodSelect.value;
        if (method === 'credit-card') {
            creditCardInfo.classList.add('active');
            paypalInfo.classList.remove('active');
        } else {
            creditCardInfo.classList.remove('active');
            paypalInfo.classList.add('active');
        }
    }

    // Redirection logic
    document.querySelectorAll('button[data-href]').forEach(button => {
        button.addEventListener('click', function() {
            window.location.href = this.dataset.href;
        });
    });
});
