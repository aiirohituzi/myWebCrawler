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
          }
        ]
      }
    }
  },
  methods: {
    fetchRatings: function () {
      axios.get('http://localhost:8000/userRatingChart/?userName=' + this.$route.params.userName).then((response) => {
        for(var i=0; i<response.data.length; i++){
          this.datacollection.labels.push(response.data[i].Update_time)
          this.datacollection.datasets[0].data.push(response.data[i].SOLO)
          this.datacollection.datasets[1].data.push(response.data[i].DUO)
          this.datacollection.datasets[2].data.push(response.data[i].SQUAD)
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