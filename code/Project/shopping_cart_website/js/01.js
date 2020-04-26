var _obj = { movie: 'Batman', year: 2003, title: 'This movie takes place in Gotham' }

// instance creation

var vm = new Vue({
    el: '#new',
    // data : _obj,
    data: {
        name: "sreeram",
    },

    methods: {
        moviefunc: function (year) {
            return year < 2000;
        }
    }
});
