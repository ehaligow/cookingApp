import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import SingleRecipe from '../components/SingleRecipe.vue';
import RecipesView from '../views/RecipesView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/recipes',
      name: 'recipes',
      component: RecipesView,
    },
    ,
    {
      path: '/recipes/:recipe_slug',
      name: 'singleRecipe',
      component: SingleRecipe,
    }
  ],
})

export default router
