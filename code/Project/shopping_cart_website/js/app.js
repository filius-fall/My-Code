// import Vue from 'vue'
var vm = new Vue({
    el: '#new',
    data: {
        firstname: 'Sreeram',
        lastname: 'ambalam',
        address: 'anantapur',
        password: '',
    },
    methods: {
        mydetails: function () {
            return "I am" + " " + this.firstname + " " + this.lastname;
        }
    },
});

var app = new Vue({
    el: '#app',

    data: {
        message: 'Hello Vue!',
        name: 'sreeram',
        movies: ['Batman', 'Dark Knight'],
        actors: [{ name: 'christian bale', role: 'batman' }, { name: 'heath ledger', role: 'joker' }],

    }
});

var app1 = new Vue({
    el: '#app1',

    data: {
        numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],

    },

    methods: {
        changenumber: function () {
            Vue.set(this.numbers, 2, 10);
            alert(this.numbers[2])
        }
    },
});

var name = new Vue({
    el: "#name",

    data: {
        counter: 1,
        fname: 'filius',
        lname: 'fall',
    },
    methods: {
        changename: function () {
            this.fname = "sree";
            this.lname = "Ram";
        },
        changesetter: function () {
            this.fullname = 'sree Ram';
        }
    },
    computed: {
        fullname: {
            get: function () {
                alert("Getting Value");
                return this.fname + ' ' + this.lname;
            },
            set: function (newvalue) {
                alert("setting New name......" + newvalue);
                var pass = newvalue.split(' ');
                this.fname = pass[0];
                this.lname = pass[pass.lenght - 1];
            }
        }

    }
});

var watcher = new Vue({
    el: "#watchers",
    data: {
        searchQuery: '',
        results: [],
        isSearching: false,
    },
    watch: {
        searchQuery: function (query) {
            console.log(query);
        }
    }
});

var example = new Vue({
    el: "#exmple",
    data: {
        movies: [
            { name: 'Batman', year: '2005' },
            { name: 'Dark Knight', year: '2008' },
            { name: 'Dark Knight Rises', year: '2010' }
        ]
    },

    methods: {
        addMovie: function () {
            this.movies.push({
                name: 'NEW Batman',
                year: '2021',

            })
        },
    },

    computed: {
        formattedString: function (movies) {
            return this.movies.map(function (movie) {
                return movie.name + '(' + movie.year + ')';
            });
        }
    },

    watch: {
        movies: function (movies) {
            var newMovie = movies[movies.length - 1];
            var nm = "2";
            console.log(nm);
            console.log(newMovie);
            alert(newMovie.name + " from " + newMovie.year + " was just added");
        }
    },
});

var fter = new Vue({
    el: "#fter",
    data: {
        message: "i am batman",
    },
    filters: {
        uppercase: function (value, firstLetter) {
            if (!value) {
                return '';
            }
            value = value.toString();
            if (firstLetter) {
                return value.charAt(0).toUpperCase() + value.slice(1);
            }
            else {
                return value.toUpperCase();
            }
        }
    }
});