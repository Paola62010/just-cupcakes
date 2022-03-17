var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: 'Montserrat, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

//Validaiton errors on card element

card.addEventListener('change', function(event){
    var errorDiv = document.getElementById('card-errors');
    if(event.error){
        var htmlContent = `
        <span>
            <i class="bi bi-exclamation-triangle-fill"></i>
        </span>
        <span>${event.error.message}</span>`;
        $(errorDiv).html(htmlContent);
    } else{
        errorDiv.textContent = '';
    }
});

// Checkout form submission

form.addEventListener('submit', function(e){
    e.preventDefault();
    card.update({'disabled': true});
    $('#order-submit').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result){
        if (result.error){
            var errorDiv = document.getElementById('card-errors');
            var htmlContent = `
                <span>
                    <i class="bi bi-exclamation-triangle-fill"></i>
                </span>
                <span>${event.error.message}</span>`;
            $(errorDiv).html(htmlContent);
            card.update({'disabled': false});
            $('#order-submit').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded'){
                form.submit()
            }
        }
    })
})