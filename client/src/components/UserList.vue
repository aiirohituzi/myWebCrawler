<template>
<div id="UserList">
    <div class="container">
        <h1>등록된 유저 목록</h1>
        <div class="list-group">
            <a v-for="user in userList" :user="user" @click="userRating(user)" class="list-group-item">
                {{ user }}
            </a>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UserList',
    data () {
        return {
            userList: []
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchUserList: function () {
            console.log('asdf')
            axios.get('http://localhost:8000/userList/').then((response) => {
                this.userList = response.data
                console.log(userList)
            }, (error) => {
                console.log(error)
            })
        }
    },
    mounted: function () {
        this.fetchUserList()
    }
}
</script>

<style>

</style>