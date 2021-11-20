<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloAikatsu :api="api"/>
  </div>
</template>

<script>
import HelloAikatsu from './components/HelloAikatsu.vue'

export default {
  name: 'App',
  components: {
    HelloAikatsu
  },
  data() {
    return {
      api: process.env.VUE_APP_API_URL,
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
