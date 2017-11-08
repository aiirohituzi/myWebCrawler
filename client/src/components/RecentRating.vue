<template>
<div id="RecentRating">
    <div class="container">
        <h1>최근 레이팅</h1>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th @click="sorting('USER')">USER</th>
                    <th @click="sorting('SOLO')">SOLO</th>
                    <th @click="sorting('DUO')">DUO</th>
                    <th @click="sorting('SQUAD')">SQUAD</th>
                    <th @click="sorting('SOLOFPP')">SOLO-FPP</th>
                    <th @click="sorting('DUOFPP')">DUO-FPP</th>
                    <th @click="sorting('SQUADFPP')">SQUAD-FPP</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="rating in r_ratings" @click="userRating(rating.USER)">
                    <td>{{ rating.USER }} <span class="label label-info">{{rating.season}}</span></td>
                    <td>{{ rating.SOLO }}</td>
                    <td>{{ rating.DUO }}</td>
                    <td>{{ rating.SQUAD }}</td>
                    <td>{{ rating.SOLOFPP }}</td>
                    <td>{{ rating.DUOFPP }}</td>
                    <td>{{ rating.SQUADFPP }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RecentRating',
    data () {
        return {
            r_ratings: []
        }
    },
    methods: {
        userRating: function (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/recentRating/').then((response) => {
                this.r_ratings = response.data
            }, (error) => {
                console.log(error)
            })
        },
        sorting: function (Sortby) {
            switch (Sortby) {
                case "USER":
                    this.r_ratings.sort(function (a,b){
                        return(a.USER.toLowerCase() < b.USER.toLowerCase()) ? -1 : (a.USER.toLowerCase() > b.USER.toLowerCase()) ? 1 : 0
                    })
                    break;
                case "SOLO":
                    this.r_ratings.sort(function (a,b){
                        return(a.SOLO > b.SOLO) ? -1 : (a.SOLO < b.SOLO) ? 1 : (a.SOLO == undefined) ? 1 : (b.SOLO == undefined) ? -1 : 0
                    })
                    break;
                case "DUO":
                    this.r_ratings.sort(function (a,b){
                        return(a.DUO > b.DUO) ? -1 : (a.DUO < b.DUO) ? 1 : (a.DUO == undefined) ? 1 : (b.DUO == undefined) ? -1 : 0
                    })
                    break
                case "SQUAD":
                    this.r_ratings.sort(function (a,b){
                        return(a.SQUAD > b.SQUAD) ? -1 : (a.SQUAD < b.SQUAD) ? 1 : (a.SQUAD == undefined) ? 1 : (b.SQUAD == undefined) ? -1 : 0
                    })
                    break
                case "SOLOFPP":
                    this.r_ratings.sort(function (a,b){
                        return(a.SOLOFPP > b.SOLOFPP) ? -1 : (a.SOLOFPP < b.SOLOFPP) ? 1 : (a.SOLOFPP == undefined) ? 1 : (b.SOLOFPP == undefined) ? -1 : 0
                    })
                    break
                case "DUOFPP":
                    this.r_ratings.sort(function (a,b){
                        return(a.DUOFPP > b.DUOFPP) ? -1 : (a.DUOFPP < b.DUOFPP) ? 1 : (a.DUOFPP == undefined) ? 1 : (b.DUOFPP == undefined) ? -1 : 0
                    })
                    break
                case "SQUADFPP":
                    this.r_ratings.sort(function (a,b){
                        return(a.SQUADFPP > b.SQUADFPP) ? -1 : (a.SQUADFPP < b.SQUADFPP) ? 1 : (a.SQUADFPP == undefined) ? 1 : (b.SQUADFPP == undefined) ? -1 : 0
                    })
                    break
                default:
                    console.log('sort error')
            }
        }
    },
    mounted: function () {
        this.fetchRatings()
    }
}
</script>

<style>

</style>