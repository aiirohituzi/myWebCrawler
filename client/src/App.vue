<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div class="container">
      <ul class="nav nav-pills">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/AllRating">All Rating</router-link></li>
          <li><router-link to="/RecentRating">Recent Rating</router-link></li>
          <li><router-link to="/Ranking">Ranking</router-link></li>
      </ul>
    </div>
    <router-view></router-view>
    <router-view name="option"></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
