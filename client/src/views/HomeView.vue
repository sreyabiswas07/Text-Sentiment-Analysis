<template>
  <div class="container">
    <SentimentAnalysis />
  </div>
</template>

<script>
// @ is an alias to /src
import SentimentAnalysis from "../components/SentimentAnalysis.vue";

export default {
  name: "HomeView",
  components: {
    SentimentAnalysis,
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Poppins", sans-serif;
}

.container {
  margin: 30px auto;
  overflow: auto;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
  height: 700px;
  width: 700px;
  background-color: snow;
}
</style>
