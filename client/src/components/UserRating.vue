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
            
            <tbody v-if="length==1">
                <tr>
                    <td>{{ u_ratings[0].SOLO }}</td>
                    <td>{{ u_ratings[0].DUO }}</td>
                    <td>{{ u_ratings[0].SQUAD }}</td>
                    <td>{{ u_ratings[0].SOLOFPP }}</td>
                    <td>{{ u_ratings[0].DUOFPP }}</td>
                    <td>{{ u_ratings[0].SQUADFPP }}</td>
                    <td>{{ u_ratings[0].Update_time }}</td>
                </tr>
            </tbody>

            <tbody v-else>
                <tr v-for="n in max">
                    <td>{{ u_ratings[n-1].SOLO }}</td>
                    <td>{{ u_ratings[n-1].DUO }}</td>
                    <td>{{ u_ratings[n-1].SQUAD }}</td>
                    <td>{{ u_ratings[n-1].SOLOFPP }}</td>
                    <td>{{ u_ratings[n-1].DUOFPP }}</td>
                    <td>{{ u_ratings[n-1].SQUADFPP }}</td>
                    <td>{{ u_ratings[n-1].Update_time }}</td>
                </tr>
            </tbody>
        </table>
        <button v-if="more" class="btn btn-primary btn-block" @click="moreData()">More</button>
        <button v-else class="btn btn-default btn-block" disabled="disabled">No more data...</button>
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
            u_ratings: [
               {
                   'USER': 'Unknown',
                   'SOLO': '0',
                   'DUO': '0',
                   'SQUAD': '0',
                   'SOLOFPP': '0',
                   'DUOFPP': '0',
                   'SQUADFPP': '0',
                   'Update_time': '0000-00-00 00:00:00'
               }
            ],
            length: 1,
            max: 10,
            more: true,
        }
    },
    methods: {
        fetchRatings: function () {
            axios.get('http://localhost:8000/userRating/?userName=' + this.$route.params.userName).then((response) => {
                this.u_ratings = response.data
                // console.log(this.u_ratings)
                this.length = response.data.length
                // console.log(this.length)

                if(this.length < this.max){
                    this.max = this.length
                }
            }, (error) => {
                console.log(error)
            })
        },
        moreData () {
            if(this.max+10 <= this.length) {
                this.max+=10
            } else {
                this.max = this.length
            }

            if(this.u_ratings[this.max] == undefined) {
                this.more = false
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