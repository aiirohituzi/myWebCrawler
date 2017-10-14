<template>
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2 text-left">
            <h1>PUBG 레이팅 기록용</h1>
            <p>
                주변 지인들의 배틀 그라운드 레이팅을 기록 및 조회하기 위한 개인적인 목적의 웹사이트입니다.
            </p>
        </div>
    </div>
    <hr>
    <div class="row">
        <p>다른 유저의 레이팅 정보를 찾아보고 싶다면?</p>
        <div class="input-group col-md-6 col-xs-10 col-md-offset-3 col-xs-offset-1">
            <input type="text" class="form-control" placeholder="PUBG nickname" v-model="id">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="ratingSearch(id)">Search</button>
            </span>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data () {
        return {
            id: null,
        }
    },
    methods: {
        ratingSearch: function (id) {
            window.open("https://dak.gg/profile/"+id)
            this.id = null
        }
    }
}
</script>

<style>
</style>