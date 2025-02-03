<template>
  <div>
    <h1>Recipes</h1>
    <ul>
      <li v-for="r in recipes" :key="r.id">
        <RouterLink :to="`/recipes/${r.slug}`">{{ r.title }}</RouterLink>
      </li>
    </ul>
  </div>
</template>

<style scoped>
h2 {
  color: red;
}
</style>

<script>
import RecipesList from '../components/SingleRecipe.vue'

import axios from 'axios'

export default {
  data() {
    return {
      recipes: [],
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/api/v1/recipes/')
      .then((response) => {
        this.recipes = response.data
      })
      .catch((error) => {
        console.error('Error occured', error)
      })
  },
}
</script>