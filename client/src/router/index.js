import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import AllRating from '@/components/AllRating'
import RecentRating from '@/components/RecentRating'
import UserRating from '@/components/UserRating'
import Ranking from '@/components/Ranking'
import chartTest from '@/components/chart-test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'hello',
      component: chartTest
    },
    {
      path: '/AllRating',
      name: 'AllRating',
      component: AllRating
    },
    {
      path: '/RecentRating',
      name: 'RecentRating',
      component: RecentRating
    },
    {
      path: '/UserRating/:userName',
      name: 'UserRating',
      component: UserRating,
      props: true
    },
    {
      path: '/Ranking',
      name: 'Ranking',
      component: Ranking
    },
  ]
})
