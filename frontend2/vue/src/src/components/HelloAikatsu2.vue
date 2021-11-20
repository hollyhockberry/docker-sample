<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloAikatsu2',
  props: {
    api: String
  },
  data() {
    return {
      message: '',
    }
  },
  mounted() {
    this.loadMessage()

    setInterval(() => {
      this.message = this.upperLower(this.message)
    }, 100)
    setInterval(() => {
      this.loadMessage()
    }, 5000)
  },
  methods: {
    loadMessage() {
      this.axios.get(this.api)
      .then(response => this.message = response.data.Message)
    },
    upperLower(str) {
      function* ulg(str) {
        for (var c of [...str]) {
          if (c.search(/[^A-Za-z]/) == -1) {
            yield ((Math.floor(Math.random() * 10) >= 5) ? c.toLowerCase() : c)
          } else {
            yield c
          }
        }
      }
      var s = ''
      for (var c of ulg(str.toUpperCase())) {
        s += c
      }
      return s
    }
  }
}
</script>
