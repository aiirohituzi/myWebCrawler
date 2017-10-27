<template>
<div id="UserRating">
    <div class="container">
        <h1>{{ userName }} 의 전체 레이팅 <button class="btn btn-default btn-xs" @click="detail()">상세보기</button></h1>
        <div class="col-md-4 col-md-offset-8">
            <div class="panel panel-default">
                <div class="panel-heading">최근 K / D 수치</div>
                <table class="table table-condensed">
                    <thead>
                        <tr>
                            <th>SOLO</th>
                            <th>DUO</th>
                            <th>SQUAD</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td v-if="u_ratings[0].SOLOKD != null">{{u_ratings[0].SOLOKD}}</td>
                            <td v-else>-</td>
                            <td v-if="u_ratings[0].DUOKD != null">{{u_ratings[0].DUOKD}}</td>
                            <td v-else>-</td>
                            <td v-if="u_ratings[0].SQUADKD != null">{{u_ratings[0].SQUADKD}}</td>
                            <td v-else>-</td>
                        </tr>
                    </tbody>
                </table>
                <table class="table table-condensed">
                    <thead>
                        <tr>
                            <th>SOLO-FPP</th>
                            <th>DUO-FPP</th>
                            <th>SQUAD-FPP</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td v-if="u_ratings[0].SOLOFPPKD != null">{{u_ratings[0].SOLOFPPKD}}</td>
                            <td v-else>-</td>
                            <td v-if="u_ratings[0].DUOFPPKD != null">{{u_ratings[0].DUOFPPKD}}</td>
                            <td v-else>-</td>
                            <td v-if="u_ratings[0].SQUADFPPKD != null">{{u_ratings[0].SQUADFPPKD}}</td>
                            <td v-else>-</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="pull-left">
            <button class="btn btn-default" @click="seasonChange('시즌 3')">시즌 3</button>
            <button class="btn btn-default" @click="seasonChange('시즌 4')">시즌 4</button>
            <button class="btn btn-default" @click="seasonChange('시즌 5')">시즌 5</button>
        </div>
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
        fetchRatings: function (season) {
            axios.get('http://localhost:8000/userRating/?userName=' + this.$route.params.userName + '&season=' + season).then((response) => {
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
        seasonChange: function(season) {
            this.$router.push({name:'UserRating', params:{userName:this.userName, season:season}})
            this.length = 1
            this.max = 10
            this.more = true
            console.log(this.$route.params.season)
            this.fetchRatings(season)
        },
        moreData: function () {
            if(this.max+10 <= this.length) {
                this.max+=10
            } else {
                this.max = this.length
            }

            if(this.u_ratings[this.max] == undefined) {
                this.more = false
            }
        },
        detail: function() {
            window.open("https://dak.gg/profile/"+this.userName)
        }
    },
    mounted: function () {
        this.fetchRatings()
    }
}
</script>

<style>

</style>