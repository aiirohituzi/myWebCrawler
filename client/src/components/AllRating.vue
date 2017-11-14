<template>
<div id="AllRating">
    <div class="container table-responsive">
        <h1>전체 레이팅 기록</h1>
        <div>
            <span v-if="this.error" class="label label-danger">서버 연결 에러</span>
        </div>
        <div class="pull-left">
            <button v-if="this.season != undefined" class="btn btn-default" @click="seasonChange(undefined)">전체 보기</button>
            <button v-else class="btn btn-primary" @click="seasonChange(undefined)">전체 보기</button>

            <button v-if="this.season != '시즌 3'" class="btn btn-default" @click="seasonChange('시즌 3')">시즌 3</button>
            <button v-else class="btn btn-primary" @click="seasonChange('시즌 3')">시즌 3</button>

            <button v-if="this.season != '시즌 4'" class="btn btn-default" @click="seasonChange('시즌 4')">시즌 4</button>
            <button v-else class="btn btn-primary" @click="seasonChange('시즌 4')">시즌 4</button>

            <button v-if="this.season != '시즌 5'" class="btn btn-default" @click="seasonChange('시즌 5')">시즌 5</button>
            <button v-else class="btn btn-primary" @click="seasonChange('시즌 5')">시즌 5</button>
        </div>
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

            <tbody v-if="length==1" @click="userRating(ratings[0].USER)">
                <tr>
                    <td>{{ ratings[0].USER }}</td>
                    <td>{{ ratings[0].SOLO }}</td>
                    <td>{{ ratings[0].DUO }}</td>
                    <td>{{ ratings[0].SQUAD }}</td>
                    <td>{{ ratings[0].SOLOFPP }}</td>
                    <td>{{ ratings[0].DUOFPP }}</td>
                    <td>{{ ratings[0].SQUADFPP }}</td>
                    <td><span class="label label-info">{{ratings[0].season}}</span> {{ ratings[0].Update_time }}</td>
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
                    <td><span class="label label-info">{{ratings[n-1].season}}</span> {{ ratings[n-1].Update_time }}</td>
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
            season: undefined,
            ratings: [
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
            error: false
        }
    },
    methods: {
        userRating: function (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            var season = ''
            if(this.season){
                season = '?season=' + this.season
            }
            axios.get('http://localhost:8000/rating/'+season).then((response) => {
                this.error = false
                this.ratings = response.data
                this.length = response.data.length

                if(this.length < this.max){
                    this.max = this.length
                }
            }, (error) => {
                console.log(error)
                this.error = true
            })
        },
        moreData: function () {
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
        },
        seasonChange: function(season) {
            this.season = season
            this.length = 1
            this.max = 10
            this.more = true
            this.fetchRatings()
        },
    },
    mounted: function () {
        this.fetchRatings()
    }
}
</script>

<style>
</style>