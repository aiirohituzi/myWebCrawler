import Vue from 'vue'
import VueRouter from 'vue-router'
import Hello from '@/components/Hello'
import AllRating from '@/components/AllRating'
import RecentRating from '@/components/RecentRating'
import UserRating from '@/components/UserRating'
import Ranking from '@/components/Ranking'
import ChartTest from '@/components/chart-test'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'hello',
      component: Hello
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
      components: {
        default: UserRating,
        option: ChartTest
      },
      props: true
    },
    {
      path: '/Ranking',
      name: 'Ranking',
      component: Ranking
    },
    {
      path: '/ChartTest/:userName',
      name: 'ChartTest',
      component: ChartTest,
      props: true
    },
  ]
})
