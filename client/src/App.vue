<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div class="container">
      <ul class="nav nav-pills">
          <router-link tag="li" to="/" exact><a>Home</a></router-link>
          <router-link tag="li" to="/AllRating" exact><a>All Rating</a></router-link>
          <router-link tag="li" to="/RecentRating" exact><a>Recent Rating</a></router-link>
          <router-link tag="li" to="/Ranking" exact><a>Ranking</a></router-link>
          <router-link tag="li" to="/UserList" exact><a>UserList</a></router-link>
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
