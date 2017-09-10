import Vue from 'vue'
import Router from 'vue-router'
// import Hello from '@/components/Hello'
import AllRating from '@/components/AllRating'
import RecentRating from '@/components/RecentRating'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllRating',
      component: AllRating
    },
    {
      path: '/:name',
      name: 'RecentRating',
      component: RecentRating
    }
  ]
})
