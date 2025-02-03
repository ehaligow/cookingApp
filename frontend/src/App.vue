<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="Cooking App" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/recipes">Recipes</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  border-bottom: 1px;
  margin-bottom: 1rem;
}

h1 {
  text-align: center;
  font-weight: bolder;
  margin-bottom: 1rem;
}

nav {
  text-align: center;
  margin-top: 1rem;
}

nav a {
  text-align: center;
  padding: 0 1rem;
  margin: 1rem;
}
</style>
