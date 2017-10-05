<template>
<div id="RecentRating">
    <div class="container">
        <h1>{{ userName }} 의 전체 레이팅</h1>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>SOLO</th>
                    <th>DUO</th>
                    <th>SQUAD</th>
                    <th>SOLO-FPP</th>
                    <th>DUO-FPP</th>
                    <th>SQUAD-FPP</th>
                    <th>Update time</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="rating in u_ratings" :rating="rating">
                    <td>{{ rating.SOLO }}</td>
                    <td>{{ rating.DUO }}</td>
                    <td>{{ rating.SQUAD }}</td>
                    <td>{{ rating.SOLOFPP }}</td>
                    <td>{{ rating.DUOFPP }}</td>
                    <td>{{ rating.SQUADFPP }}</td>
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
    name: 'UserRating',
    data () {
        return {
            userName: this.$route.params.userName,
            u_ratings: []
        }
    },
    methods: {
        fetchRatings: function () {
            axios.get('http://localhost:8000/userRating/?userName=' + this.$route.params.userName).then((response) => {
                this.u_ratings = response.data
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