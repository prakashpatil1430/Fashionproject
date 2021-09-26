$('#slider1').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 4,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    console.log(id);
    $.ajax(
        {
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data);
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount.toFixed(2);
                document.getElementById("total_amount").innerText = data.total_amount.toFixed(2);
            }
        }) 
});

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax(
        {
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data)
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount.toFixed(2);
                document.getElementById("total_amount").innerText = data.total_amount.toFixed(2);
            }
        })
});

