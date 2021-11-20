<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloAikatsu2 :api="api"/>
  </div>
</template>

<script>
import HelloAikatsu2 from './components/HelloAikatsu2.vue'

export default {
  name: 'App',
  components: {
    HelloAikatsu2
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
  font-family: monospace, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
