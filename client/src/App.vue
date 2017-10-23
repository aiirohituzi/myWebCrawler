<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div class="container">
      <nav class="navbar navbar-default visible-xs-block navbar-fixed-top">
        <div class="container-fluid">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">PUBG</a>
          </div>

          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
              <router-link tag="li" to="/" exact><a>Home</a></router-link>
              <router-link tag="li" to="/AllRating" exact><a>All Rating</a></router-link>
              <router-link tag="li" to="/RecentRating" exact><a>Recent Rating</a></router-link>
              <router-link tag="li" to="/Ranking" exact><a>Ranking</a></router-link>
              <router-link tag="li" to="/UserList" exact><a>UserList</a></router-link>
            </ul>
          </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
      </nav>
      <ul class="nav nav-pills hidden-xs">
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
