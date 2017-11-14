<template>
<div id="RecentRating">
    <div class="container table-responsive">
        <h1>최근 레이팅</h1>
        <div>
            <span v-if="this.error" class="label label-danger">서버 연결 에러</span>
        </div>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th @click="sorting('USER')">USER {{sort_header[0]}}</th>
                    <th @click="sorting('SOLO')">SOLO {{sort_header[1]}}</th>
                    <th @click="sorting('DUO')">DUO {{sort_header[2]}}</th>
                    <th @click="sorting('SQUAD')">SQUAD {{sort_header[3]}}</th>
                    <th @click="sorting('SOLOFPP')">SOLO-FPP {{sort_header[4]}}</th>
                    <th @click="sorting('DUOFPP')">DUO-FPP {{sort_header[5]}}</th>
                    <th @click="sorting('SQUADFPP')">SQUAD-FPP {{sort_header[6]}}</th>
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
            r_ratings: [
               {
                   'USER': 'Unknown',
                   'SOLO': '0',
                   'DUO': '0',
                   'SQUAD': '0',
                   'SOLOFPP': '0',
                   'DUOFPP': '0',
                   'SQUADFPP': '0',
               }
            ],
            sort_header: [
                '', '', '', '', '', '', ''
            ],
            error: false
        }
    },
    methods: {
        userRating: function (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/recentRating/').then((response) => {
                this.error = false
                this.r_ratings = response.data
            }, (error) => {
                console.log(error)
                this.error = true
            })
        },
        sorting: function (Sortby) {
            switch (Sortby) {
                case "USER":
                    if(this.sort_header[0] != '▲'){
                        this.r_ratings.sort(function (a,b){
                            return(a.USER.toLowerCase() < b.USER.toLowerCase()) ? -1 : (a.USER.toLowerCase() > b.USER.toLowerCase()) ? 1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[0] = '▲'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.USER.toLowerCase() > b.USER.toLowerCase()) ? -1 : (a.USER.toLowerCase() < b.USER.toLowerCase()) ? 1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[0] = '▼'
                    }
                    break;
                case "SOLO":
                    if(this.sort_header[1] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.SOLO > b.SOLO) ? -1 : (a.SOLO < b.SOLO) ? 1 : (a.SOLO == undefined) ? 1 : (b.SOLO == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[1] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.SOLO < b.SOLO) ? -1 : (a.SOLO > b.SOLO) ? 1 : (a.SOLO == undefined) ? 1 : (b.SOLO == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[1] = '▲'
                    }
                    break;
                case "DUO":
                    if(this.sort_header[2] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.DUO > b.DUO) ? -1 : (a.DUO < b.DUO) ? 1 : (a.DUO == undefined) ? 1 : (b.DUO == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[2] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.DUO < b.DUO) ? -1 : (a.DUO > b.DUO) ? 1 : (a.DUO == undefined) ? 1 : (b.DUO == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[2] = '▲'
                    }
                    break
                case "SQUAD":
                    if(this.sort_header[3] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.SQUAD > b.SQUAD) ? -1 : (a.SQUAD < b.SQUAD) ? 1 : (a.SQUAD == undefined) ? 1 : (b.SQUAD == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[3] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.SQUAD < b.SQUAD) ? -1 : (a.SQUAD > b.SQUAD) ? 1 : (a.SQUAD == undefined) ? 1 : (b.SQUAD == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[3] = '▲'
                    }
                    break
                case "SOLOFPP":
                    if(this.sort_header[4] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.SOLOFPP > b.SOLOFPP) ? -1 : (a.SOLOFPP < b.SOLOFPP) ? 1 : (a.SOLOFPP == undefined) ? 1 : (b.SOLOFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[4] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.SOLOFPP < b.SOLOFPP) ? -1 : (a.SOLOFPP > b.SOLOFPP) ? 1 : (a.SOLOFPP == undefined) ? 1 : (b.SOLOFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[4] = '▲'
                    }
                    break
                case "DUOFPP":
                    if(this.sort_header[5] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.DUOFPP > b.DUOFPP) ? -1 : (a.DUOFPP < b.DUOFPP) ? 1 : (a.DUOFPP == undefined) ? 1 : (b.DUOFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[5] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.DUOFPP < b.DUOFPP) ? -1 : (a.DUOFPP > b.DUOFPP) ? 1 : (a.DUOFPP == undefined) ? 1 : (b.DUOFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[5] = '▲'
                    }
                    break
                case "SQUADFPP":
                    if(this.sort_header[6] != '▼'){
                        this.r_ratings.sort(function (a,b){
                            return(a.SQUADFPP > b.SQUADFPP) ? -1 : (a.SQUADFPP < b.SQUADFPP) ? 1 : (a.SQUADFPP == undefined) ? 1 : (b.SQUADFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[6] = '▼'
                    } else {
                        this.r_ratings.sort(function (a,b){
                            return(a.SQUADFPP < b.SQUADFPP) ? -1 : (a.SQUADFPP > b.SQUADFPP) ? 1 : (a.SQUADFPP == undefined) ? 1 : (b.SQUADFPP == undefined) ? -1 : 0
                        })
                        this.sort_header = ['', '', '', '', '', '', '']
                        this.sort_header[6] = '▲'
                    }
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