<template>
<div id="Ranking" class="container">
    <div class="pull-left">
        <button v-if="this.season != '시즌 3'" class="btn btn-default" @click="seasonChange('시즌 3')">시즌 3</button>
        <button v-else class="btn btn-primary" @click="seasonChange('시즌 3')">시즌 3</button>

        <button v-if="this.season != '시즌 4'" class="btn btn-default" @click="seasonChange('시즌 4')">시즌 4</button>
        <button v-else class="btn btn-primary" @click="seasonChange('시즌 4')">시즌 4</button>

        <button v-if="(this.season != '시즌 5') && (this.season != undefined)" class="btn btn-default" @click="seasonChange('시즌 5')">시즌 5</button>
        <button v-else class="btn btn-primary" @click="seasonChange('시즌 5')">시즌 5</button>
    </div>
    <br>
    <h1>3인칭 랭킹</h1>
    <div>
        <span v-if="this.error" class="label label-danger">서버 연결 에러</span>
    </div>
    <hr>
    <div class="row">
        <div class="col-md-6 table-responsive">
            <h3>SOLO RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO</th>
                        <th>DUO</th>
                        <th>SQUAD</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in s_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td><b>{{ rating.SOLO }}</b></td>
                        <td>{{ rating.DUO }}</td>
                        <td>{{ rating.SQUAD }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-6 table-responsive">
            <h3>DUO RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO</th>
                        <th>DUO</th>
                        <th>SQUAD</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in d_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLO }}</td>
                        <td><b>{{ rating.DUO }}</b></td>
                        <td>{{ rating.SQUAD }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-12 table-responsive">
            <h3>SQUAD RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO</th>
                        <th>DUO</th>
                        <th>SQUAD</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in q_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLO }}</td>
                        <td>{{ rating.DUO }}</td>
                        <td><b>{{ rating.SQUAD }}</b></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <h1>1인칭 랭킹</h1>
    <hr>
    <div class="row">
        <div class="col-md-6 table-responsive">
            <h3>SOLO-FPP RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO-FPP</th>
                        <th>DUO-FPP</th>
                        <th>SQUAD-FPP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in sf_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td><b>{{ rating.SOLOFPP }}</b></td>
                        <td>{{ rating.DUOFPP }}</td>
                        <td>{{ rating.SQUADFPP }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-6 table-responsive">
            <h3>DUO-FPP RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO-FPP</th>
                        <th>DUO-FPP</th>
                        <th>SQUAD-FPP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in df_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLOFPP }}</td>
                        <td><b>{{ rating.DUOFPP }}</b></td>
                        <td>{{ rating.SQUADFPP }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-12 table-responsive">
            <h3>SQUAD-FPP RANKING</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th></th>
                        <th>USER</th>
                        <th>SOLO-FPP</th>
                        <th>DUO-FPP</th>
                        <th>SQUAD-FPP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(rating, index) in qf_ratings" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLOFPP }}</td>
                        <td>{{ rating.DUOFPP }}</td>
                        <td><b>{{ rating.SQUADFPP }}</b></td>
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
    name: 'Ranking',
    data () {
        return {
            season: undefined,
            TPP_ratings: [],
            s_ratings: [],
            d_ratings: [],
            q_ratings: [],
            FPP_ratings: [],
            sf_ratings: [],
            df_ratings: [],
            qf_ratings: [],
            error: false
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/TPPRanking/?season=' + this.season).then((response) => {
                this.error = false
                this.TPP_ratings = response.data
                // console.log(response)
                this.s_ratings = []
                this.d_ratings = []
                this.q_ratings = []
                for(var i=0; i<this.TPP_ratings.length; i++){
                    this.s_ratings.push(this.TPP_ratings[i])
                    this.d_ratings.push(this.TPP_ratings[i])
                    this.q_ratings.push(this.TPP_ratings[i])
                }
                this.s_ratings.sort(function (a,b){
                    return(a.SOLO > b.SOLO) ? -1 : (a.SOLO < b.SOLO) ? 1 : 0
                })
                this.d_ratings.sort(function (a,b){
                    return(a.DUO > b.DUO) ? -1 : (a.DUO < b.DUO) ? 1 : 0
                })
                this.q_ratings.sort(function (a,b){
                    return(a.SQUAD > b.SQUAD) ? -1 : (a.SQUAD < b.SQUAD) ? 1 : 0
                })
            }, (error) => {
                console.log(error)
                this.error = true
            })

            // axios.get('http://localhost:8000/soloRanking/?season=' + this.season).then((response) => {
            //     this.s_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })
            
            // axios.get('http://localhost:8000/duoRanking/?season=' + this.season).then((response) => {
            //     this.d_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })

            // axios.get('http://localhost:8000/squadRanking/?season=' + this.season).then((response) => {
            //     this.q_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })



            axios.get('http://localhost:8000/FPPRanking/?season=' + this.season).then((response) => {
                this.FPP_ratings = response.data
                // console.log(response)
                this.sf_ratings = []
                this.df_ratings = []
                this.qf_ratings = []
                for(var i=0; i<this.FPP_ratings.length; i++){
                    this.sf_ratings.push(this.FPP_ratings[i])
                    this.df_ratings.push(this.FPP_ratings[i])
                    this.qf_ratings.push(this.FPP_ratings[i])
                }
                this.sf_ratings.sort(function (a,b){
                    return(a.SOLOFPP > b.SOLOFPP) ? -1 : (a.SOLOFPP < b.SOLOFPP) ? 1 : 0
                })
                this.df_ratings.sort(function (a,b){
                    return(a.DUOFPP > b.DUOFPP) ? -1 : (a.DUOFPP < b.DUOFPP) ? 1 : 0
                })
                this.qf_ratings.sort(function (a,b){
                    return(a.SQUADFPP > b.SQUADFPP) ? -1 : (a.SQUADFPP < b.SQUADFPP) ? 1 : 0
                })
            }, (error) => {
                console.log(error)
            })

            // axios.get('http://localhost:8000/solofppRanking/?season=' + this.season).then((response) => {
            //     this.sf_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })
            
            // axios.get('http://localhost:8000/duofppRanking/?season=' + this.season).then((response) => {
            //     this.df_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })

            // axios.get('http://localhost:8000/squadfppRanking/?season=' + this.season).then((response) => {
            //     this.qf_ratings = response.data
            //     // console.log(response)
            // }, (error) => {
            //     console.log(error)
            // })
        },
        seasonChange: function(season) {
            this.season = season
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