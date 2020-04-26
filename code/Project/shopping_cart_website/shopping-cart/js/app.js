const products = [
	{id: 1,title: 'Macbook Pro', price: 2500.00, qty: 1, image: 'http://lorempixel.com/150/150/'},  
	{id: 2,title: 'Asus ROG Gaming',price: 1000.00, qty: 1,image: 'http://lorempixel.com/150/150/'},  
	{id: 3,title: 'Amazon Kindle',price: 150.00,qty: 1,image: 'http://lorempixel.com/150/150/'},  
	{id: 4,title: 'Another Product',price: 10, qty: 1, image: 'http://lorempixel.com/150/150/'},  
];

function formatNumber(n, c, d, t){
	var c = isNaN(c = Math.abs(c)) ? 2 : c, 
			d = d === undefined ? '.' : d, 
			t = t === undefined ? ',' : t, 
			s = n < 0 ? '-' : '', 
			i = String(parseInt(n = Math.abs(Number(n) || 0).toFixed(c))), 
			j = (j = i.length) > 3 ? j % 3 : 0;
	return s + (j ? i.substr(0, j) + t : '') + i.substr(j).replace(/(\d{3})(?=\d)/g, '$1' + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : '');
};

// Allow the formatNumber function to be used as a filter
Vue.filter('formatCurrency', function (value) {
	return formatNumber(value, 2, '.', ',');
});

// The shopping cart component
Vue.component('shopping-cart', {
  props: ['items'],

  computed: {
    Total() {
      let total = 0;
      this.items.forEach(item => {
        total += (item.price * item.qty);
      });
      return total;
    }
  },

  methods: {
		// Remove item by its index
    removeItem(index) {
      this.items.splice(index, 1)
    }
  }
})

const vm = new Vue({
  el: '#app',
	
  data: {
    cartItems: [],
    items : products
  },
	
  methods: {
		// Add Items to cart
    addToCart(itemToAdd) {
      let found = false;

      // Add the item or increase qty
			let itemInCart = this.cartItems.filter(item => item.id===itemToAdd.id);
			let isItemInCart = itemInCart.length > 0;

      if (isItemInCart === false) {
        this.cartItems.push(Vue.util.extend({}, itemToAdd));
      } else {
				itemInCart[0].qty += itemToAdd.qty;
			}
			
			itemToAdd.qty = 1;
    }
  }
})

