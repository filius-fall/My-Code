var vm = new Vue({
    el: '#app',
    data: {
        groupwrapper: "list-group-item",
        isShowingCart: false,
        cart: {
            items: []
        },
        name: "sreeram",
        products: [
            {
                id: 1,
                name: "MacBook Pro(15 inch)",
                description: "This laptop has super crisp Display. yeah and we know its overpriced",
                price: 250000,
                instock: 50,
            },
            {
                id: 2,
                name: "Samsung Galaxy S7 Pro",
                description: "unlike MacBook we are selling this cheap. but i may explode.... ",
                price: 35000,
                instock: 755,
            },
            {
                id: 3,
                name: "HP Office Jet 5740",
                description: "This Might not Last for very long hey but printers never works anyway...",
                price: 11600,
                instock: 5,
            },
            {
                id: 4,
                name: "iPhone 7 cover",
                description: "having trouble holding phone. Have you considered not dropping it...",
                price: 3000,
                instock: 42,
            },
            {
                id: 5,
                name: "iPad Pro(9 inch)",
                description: "We heard its supposed to br good. Atleast thats what people say.....",
                price: 47000,
                instock: 0,
            },
            {
                id: 6,
                name: "OnePlus 4 Cover",
                description: "Does your phone always spend time on the ground, then this cheap piece of plastic is the solution",
                price: 1400,
                instock: 81,
            },
        ]
    },
    filters: {
        currency: function (value) {
            var formatter = new Intl.NumberFormat("en-US", {
                style: "currency",
                currency: "INR",
                minimumFractionDigits: 0
            });
            return formatter.format(value);
        }
    },
    computed: {
        cartTotal: function () {
            var total = 0;
            this.cart.items.forEach(function (item) {
                total += item.quantity * item.product.price;
                console.log(total);
            });
            return parseInt(total);
        },
        taxAmount: function () {
            return this.cartTotal * 10 / 100;
        }
    },
    methods: {

        removeItemFromCart: function (cartItem) {
            var index = this.cart.items.indexOf(cartItem);

            if (index !== -1) {
                this.cart.items.splice(index, 1);
                ss = this.cart.items.slice(index, 1);
                console.log(ss);
            }
        },
        addProductToCart: function (product) {
            var cartItem = this.getCartItem(product);

            if (cartItem != null) {
                cartItem.quantity++;
            } else {
                this.cart.items.push({
                    product: product,
                    quantity: 1,
                });
            }
            product.instock--;
        },
        getCartItem: function (product) {
            for (var i = 0; i < this.cart.items.length; i++) {
                if (this.cart.items[i].product.id == product.id) {
                    return this.cart.items[i];
                }
            }
            return null;
        },
        increaseQunatity: function (cartItem) {
            cartItem.product.instock--;
            cartItem.quantity++;
        },
        decreaseQunatity: function (cartItem) {
            cartItem.product.instock++;
            cartItem.quantity--;
            if (cartItem.quantity == 0) {
                this.removeItemFromCart(cartItem);
            }
        },

        listwrapper: function () {
            this.groupwrapper = "list-group-item";
        },
        gridwrapper: function () {
            this.groupwrapper = "grid-group-item";
        },
        checkout: function () {

            if (confirm('Are you Sure')) {
                this.cart.items.forEach(function (item) {
                    item.product.instock += item.quantity;
                });

                this.cart.items = [];
            }
        }
    }

});

