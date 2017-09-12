<template>
<div>
<h1>각 분야 랭킹</h1>
<div id="SoloRanking">
    <div class="container">
        <h3>SOLO RANKING</h3>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>USER</th>
                    <th>SOLO</th>
                    <th>DUO</th>
                    <th>SQUAD</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="rating in ratings" :rating="rating" @click="userRating(rating.USER)">
                    <td>{{ rating.USER }}</td>
                    <td>{{ rating.SOLO }}</td>
                    <td>{{ rating.DUO }}</td>
                    <td>{{ rating.SQUAD }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SoloRanking',
    data () {
        return {
            ratings: []
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/soloRanking/').then((response) => {
                this.ratings = response.data
                console.log(response)
            }, (error) => {
                console.log(error)
            })
        }
    },
    mounted: function () {
        this.fetchRatings()
    }
}
</script>

<style>
</style>