<template>
<div id="Ranking" class="container">
    <h1>3인칭 랭킹</h1>
    <hr>
    <div class="row">
        <div class="col-md-6">
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
                    <tr v-for="(rating, index) in s_ratings" :rating="rating" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td><b>{{ rating.SOLO }}</b></td>
                        <td>{{ rating.DUO }}</td>
                        <td>{{ rating.SQUAD }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-6">
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
                    <tr v-for="(rating, index) in d_ratings" :rating="rating" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLO }}</td>
                        <td><b>{{ rating.DUO }}</b></td>
                        <td>{{ rating.SQUAD }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-12">
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
                    <tr v-for="(rating, index) in q_ratings" :rating="rating" @click="userRating(rating.USER)">
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
        <div class="col-md-6">
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
                    <tr v-for="(rating, index) in sf_ratings" :rating="rating" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td><b>{{ rating.SOLOFPP }}</b></td>
                        <td>{{ rating.DUOFPP }}</td>
                        <td>{{ rating.SQUADFPP }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-6">
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
                    <tr v-for="(rating, index) in df_ratings" :rating="rating" @click="userRating(rating.USER)">
                        <td>{{ index+1 }}</td>
                        <td>{{ rating.USER }}</td>
                        <td>{{ rating.SOLOFPP }}</td>
                        <td><b>{{ rating.DUOFPP }}</b></td>
                        <td>{{ rating.SQUADFPP }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="col-md-12">
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
                    <tr v-for="(rating, index) in qf_ratings" :rating="rating" @click="userRating(rating.USER)">
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
            s_ratings: [],
            d_ratings: [],
            q_ratings: [],
            sf_ratings: [],
            df_ratings: [],
            qf_ratings: []
        }
    },
    methods: {
        userRating (userName) {
            this.$router.push({name:'UserRating', params:{userName:userName}})
        },
        fetchRatings: function () {
            axios.get('http://localhost:8000/soloRanking/').then((response) => {
                this.s_ratings = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
            
            axios.get('http://localhost:8000/duoRanking/').then((response) => {
                this.d_ratings = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })

            axios.get('http://localhost:8000/squadRanking/').then((response) => {
                this.q_ratings = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })


            axios.get('http://localhost:8000/solofppRanking/').then((response) => {
                this.sf_ratings = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
            
            axios.get('http://localhost:8000/duofppRanking/').then((response) => {
                this.df_ratings = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })

            axios.get('http://localhost:8000/squadfppRanking/').then((response) => {
                this.qf_ratings = response.data
                // console.log(response)
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