<template>
<div id="AllRating">
    <div class="container">
        <h1>전체 레이팅 기록</h1>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>USER</th>
                    <th>SOLO</th>
                    <th>DUO</th>
                    <th>SQUAD</th>
                    <th>Update time</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="n in max" @click="userRating(ratings[n].USER)">
                    <td>{{ ratings[n].USER }}</td>
                    <td>{{ ratings[n].SOLO }}</td>
                    <td>{{ ratings[n].DUO }}</td>
                    <td>{{ ratings[n].SQUAD }}</td>
                    <td>{{ ratings[n].Update_time }}</td>
                </tr>
            </tbody>
        </table>
        <button class="btn btn-primary btn-block" @click="max+=10">More</button>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AllRating',
    data () {
        return {
            ratings: [],
            max: 10
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/rating/').then((response) => {
                this.ratings = response.data
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