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
                <tr v-for="rating in ratings" :rating="rating">
                    <td>{{ rating.USER }}</td>
                    <td>{{ rating.SOLO }}</td>
                    <td>{{ rating.DUO }}</td>
                    <td>{{ rating.SQUAD }}</td>
                    <td>{{ rating.Update_time }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AllRating',
    data () {
        return {
            ratings: []
        }
    },
    methods: {
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