<script setup lang="ts">
import HomeItem from './HomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'

const openReadmeInEditor = () => fetch('/__open-in-editor?file=README.md')
</script>

<template>
  <HomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Recipes</template>
    Explore a world of flavors with our Recipes app! 
    Easily browse, search, and discover delicious recipes tailored to your taste. 
    Whether you're craving something quick, healthy, or indulgent, find the perfect dish in just a few taps. 
    Get inspired and start cooking today!

  </HomeItem>

  <!-- <HomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading></template>

  </HomeItem> -->

</template>
