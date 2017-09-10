<template>
<div id="RecentRating">
    <div class="container">
        <h1>최근 레이팅</h1>
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
                <tr v-for="rating in r_ratings" :rating="rating">
                    <td>{{ rating.USER }}</td>
                    <td>{{ rating.SOLO }}</td>
                    <td>{{ rating.DUO }}</td>
                    <td>{{ rating.SQUAD }}</td>
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
        fetchRatings: function () {
            axios.get('http://localhost:8000/recentRating/').then((response) => {
                this.r_ratings = response.data
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