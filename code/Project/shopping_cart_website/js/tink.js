var vm = new Vue({
  el: "#tink1",
  data: {
    fname: "filius",
    lname: "fall",
    address: "Gotham",
    website: "http://sreram1729.pythonanywhere.com/",
    age: 21,
    message: "",
    selected: "",
    items: [
      { id: 1, title: "Do Something" },
      { id: 2, title: "Do Something else" },
    ],
    value1: false,
  },
  methods: {
    shouldShowThis: function () {
      return false;
    },
    handleClick: function () {
      alert("The Button is Clicked!");
    },
    keyboardclick: function () {
      alert("you have pressed Enter Button");
    },
  },
});
