<script lang="ts" setup>
  import { onMounted, computed, ref } from 'vue'
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, LineElement, PointElement } from 'chart.js'

  import axios from 'axios'

  ChartJS.register(
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    PointElement,
    CategoryScale
  )

  defineProps({
    chartId: {
      type: String,
      default: 'line-chart'
    },
    width: {
      type: Number,
      default: 1000
    },
    height: {
      type: Number,
      default: 600
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array as PropType<Plugin<'line'>[]>,
      default: () => {}
    }
  })

  const tickerLabels = ref([])
  const tickerData = ref([])
  const tickerName = ref("")
  const tickerActive = ref<string | undefined>(undefined)

  const tickers = ref([])

  const chartData = computed(() => {
    console.log("chartData computation")
    console.log(tickerData.value)
    return {
      labels: tickerLabels.value,
      datasets: [
        {
          label: tickerActive.value,
          backgroundColor: 'green',
          data: tickerData.value
        }
      ]
    }
  })

onMounted(async () => {
  await fetchTickers()
  if (tickers.value.length > 0) {
    if (tickerActive.value === undefined)
      tickerActive.value = tickers.value[0] as string
    fetchData(tickerActive.value)
  }
})

  const chartOptions = { 
    responsive: false,
    maintainAspectRatio: false
  }

  const fetchTickers = async () => {
    const resp = await axios.get('http://localhost:8000/api/tickers')
    tickers.value = resp.data
  }

  const fetchData = async (ticker_id: string) => {
    axios.get(`http://localhost:8000/api/ticker/${ticker_id}`, { params: {'limit': 20} }).then(
      (resp) => {
        const labels = resp.data.map((e) => { return e['datetime'] })
        const data = resp.data.map((e) => { return e['price'] })
        console.log(resp.data)
        tickerName.value = ticker_id
        tickerData.value = data
        tickerLabels.value = labels
      }
    )
  }

  setInterval(() => { 
    if ((tickers.value.length > 0) && (tickerActive.value !== undefined)) {
      fetchData(tickerActive.value)
    }
  }, 1000);
</script>

<template>
  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
  <label class="select" for="instrument">Select instrument:</label>

  <select class="select" id="instrument" v-model="tickerActive">
    <option
        v-for="item in tickers"
        :key="item">
      {{ item }}
    </option>
  </select>
</template>

<style scoped>
  .select {
    width: 150px;
    max-height: 80px;
    font-size: 24px;
  }
</style>