$('#popcart').popover();
updatePopover(cart);
function updatePopover(cart) {
    var popStr = "";
    popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
    var i = 1;
    for (var item in cart) {
        console.log(item);
        popStr = popStr + "<b>" + i + "</b>. ";
        if(document.getElementById('name'+item)){
             popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 19) + "... Qty: " + cart[item][0] + '<br>';
        i = i + 1;
        }

    }
    popStr = popStr + "</div> <a href='/shop/checkout'><button class='btn btn-primary' id ='checkout'>Checkout</button></a> <button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>     "
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('show');
}
