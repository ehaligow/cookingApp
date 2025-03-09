<template>
  <div v-if="recipe">
    <h3>Recipe title: {{ recipe.title }}</h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Recipe',
  data() {
    return {
      recipe: {},
      quantity: 1,
    }
  },
  mounted() {
    this.getRecipe()
  },
  methods: {
    async getRecipe() {
      const recipe_slug = this.$route.params.recipe_slug

      await axios
        .get(`http://127.0.0.1:8000/api/v1/recipes/${recipe_slug}`)
        .then((response) => {
          console.log('2here error')
          this.recipe = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>