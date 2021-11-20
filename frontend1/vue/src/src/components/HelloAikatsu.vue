<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloAikatsu',
  props: {
    api: String
  },
  data() {
    return {
      message: '',
    }
  },
  mounted() {
    setInterval(() => {
      this.axios.get(this.api)
      .then(response => this.message = response.data.Message)
    }, 1000)
  },
}
</script>
