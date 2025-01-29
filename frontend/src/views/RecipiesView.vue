<template>
  <div class="recipies">
      <h1>Recipies</h1>
      <ul>
          <li v-for="recipe in recipies" :key="recipe.id">
              {{ recipe.title }}
              {{ recipe.ingredients }}
          </li>
      </ul>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  data() {
    return {
      recipies: [],  
    };
  },
  mounted() {
    axios.get('/recipies/')
      .then(response => {
        this.recipies = response.data;
      })
      .catch(error => {
        console.error("Błąd podczas pobierania danych:", error);
      })
  }
}
/* eslint-enable */
</script>
