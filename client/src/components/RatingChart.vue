<script>
import axios from 'axios'
import { Line } from 'vue-chartjs'

export default Line.extend({
  data () {
    return {
      datacollection: {
        labels: [],
        datasets: [
          {
            label: 'Solo Rating',
            backgroundColor: '#f87979',
            data: []
          },          
          {
            label: 'Duo Rating',
            backgroundColor: '#79f879',
            data: []
          },
          {
            label: 'Squad Rating',
            backgroundColor: '#7979f8',
            data: []
          },
          {
            label: 'Solo-fpp Rating',
            backgroundColor: '#078686',
            data: []
          },          
          {
            label: 'Duo-fpp Rating',
            backgroundColor: '#860786',
            data: []
          },
          {
            label: 'Squad-fpp Rating',
            backgroundColor: '#868607',
            data: []
          }
        ]
      }
    }
  },
  methods: {
    fetchRatings: function () {
      axios.get('http://localhost:8000/userRatingChart/?userName=' + this.$route.params.userName + '&season=' + this.$route.params.season).then((response) => {
        for(var i=0; i<response.data.length; i++){
          this.datacollection.labels.push(response.data[i].Update_time)
          this.datacollection.datasets[0].data.push(response.data[i].SOLO)
          this.datacollection.datasets[1].data.push(response.data[i].DUO)
          this.datacollection.datasets[2].data.push(response.data[i].SQUAD)
          this.datacollection.datasets[3].data.push(response.data[i].SOLOFPP)
          this.datacollection.datasets[4].data.push(response.data[i].DUOFPP)
          this.datacollection.datasets[5].data.push(response.data[i].SQUADFPP)
        }
        // console.log(this.datacollection)
      }, (error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.fetchRatings()
  },
  mounted () {
    // this.fetchRatings()
    this.renderChart(this.datacollection, {responsive: true, maintainAspectRatio: false})
  }
})
</script>