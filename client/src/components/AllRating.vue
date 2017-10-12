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
                <tr v-for="n in max" @click="userRating(ratings[n-1].USER)">
                    <td>{{ ratings[n-1].USER }}</td>
                    <td>{{ ratings[n-1].SOLO }}</td>
                    <td>{{ ratings[n-1].DUO }}</td>
                    <td>{{ ratings[n-1].SQUAD }}</td>
                    <td>{{ ratings[n-1].SOLOFPP }}</td>
                    <td>{{ ratings[n-1].DUOFPP }}</td>
                    <td>{{ ratings[n-1].SQUADFPP }}</td>
                    <td>{{ ratings[n-1].Update_time }}</td>
                </tr>
            </tbody>
        </table>
        <button v-if="more" class="btn btn-primary btn-block" @click="moreData()">More</button>
        <button v-else class="btn btn-default btn-block" disabled="disabled">No more data...</button>

        <!--<pre>
            {{ratings[max-1]}}
        </pre>-->
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
            length: null,
            max: 10,
            more: true,
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/rating/').then((response) => {
                this.ratings = response.data
                this.length = response.data.length

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

            if(this.ratings[this.max] == undefined) {
                this.more = false
            }

            // console.log(this.max)
            // console.log(this.more)
        }
    },
    mounted: function () {
        this.fetchRatings()
    }
}
</script>

<style>
</style>