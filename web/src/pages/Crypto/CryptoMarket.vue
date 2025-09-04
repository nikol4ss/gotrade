<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'

import { getApiCoinGeckoOverview, getApiCoinGeckoTopCoins, getApiCoinGeckoMarketChart } from '@/services/api.coingecko.services'
import type { CoinGeckoChartData, CoinGeckoOverview, CoinGeckoCoin, CoinGeckoMarketChart } from '@/models/api.coingecko.models'

import {
  Coins,
  Percent,
  DollarSign,
  TrendingUp,
  CalendarSearch,
  LoaderCircleIcon,
  CircleQuestionMark
} from 'lucide-vue-next'

import { Toggle } from '@/components/ui/toggle'
import { Separator } from '@/components/ui/separator'

import LineChart from '@/components/charts/LineChart.vue'
import Quotation from '@/components/charts/Quotation.vue'


const overview = ref<CoinGeckoOverview>()
const quotation = ref<CoinGeckoCoin[]>([])
const marketDataMap = ref<Record<string, CoinGeckoMarketChart>>({})

const selectedDay = ref<string | null>(null)
const selectedCoins = ref<string[]>([])
const loadingOverview = ref(true)
const loadingChart = ref(false)

const chartDays = ["20", "40", "60", "80", "100"]

const chartCategories = computed(() => selectedCoins.value.map(c => c.toUpperCase()))

function parsePrice(p: unknown): number {

  if (typeof p === 'number') return Number.isFinite(p) ? p : 0;
  if (typeof p !== 'string') return 0;

  const s = p.trim();

  // pt-BR: "R$ 112.471,39"
  if (/[,]/.test(s) && !/[.]\d{2}$/.test(s)) {
    // remove tudo menos dígitos, ponto, vírgula e sinal; tira separador de milhar ".", troca "," por "."
    const normalized = s.replace(/[^\d.,-]/g, '').replace(/\./g, '').replace(',', '.');
    const n = Number(normalized);
    return Number.isFinite(n) ? n : 0;
  }

  // en-US: "$112,471.39"
  const normalized = s.replace(/[^\d.-]/g, '');
  const n = Number(normalized);
  return Number.isFinite(n) ? n : 0;
}


const chartData = computed<CoinGeckoChartData[]>(() => {
  if (!selectedDay.value || selectedCoins.value.length === 0) return [];

  const datasets = selectedCoins.value.map(
    c => marketDataMap.value[c.toLowerCase()]?.prices ?? []
  );
  if (datasets.every(d => d.length === 0)) return [];

  const maxLength = Math.max(...datasets.map(d => d.length));
  const data: CoinGeckoChartData[] = [];

  for (let i = 0; i < maxLength; i++) {
    const row: CoinGeckoChartData = {};

    row["date"] = datasets[0][i]?.date || "";

    selectedCoins.value.forEach((coin, idx) => {
      const priceItem = datasets[idx][i];
      row[coin.toUpperCase()] = priceItem ? parsePrice(priceItem.price) : 0;
    });

    data.push(row);
  }

  return data;
});

const isDisabledCrypto = (coinName: string) => selectedCoins.value.length >= 3 && !selectedCoins.value.includes(coinName)
const isDisabledDay = (day: string) => selectedDay.value !== null && selectedDay.value !== day

onMounted(async () => {
  try {
    const [overviewData, quotationData] = await Promise.all([
      getApiCoinGeckoOverview(),
      getApiCoinGeckoTopCoins()
    ])
    overview.value = overviewData
    quotation.value = quotationData
  } finally {
    loadingOverview.value = false
  }
})

watch([selectedCoins, selectedDay], async ([coins, days]) => {
  if (coins.length === 0 || !days) return
  loadingChart.value = true

  const promises = coins.map(coin =>
    getApiCoinGeckoMarketChart(coin.toLowerCase(), Number(days))
  )
  const results = await Promise.all(promises)

  coins.forEach((c, idx) => {
    marketDataMap.value[c.toLowerCase()] = results[idx]
  })

  loadingChart.value = false
})
</script>

<template>
  <div class="flex flex-1 flex-col gap-5 p-2 pt-0">
    <!-- Overview -->
    <div class="grid auto-rows-min gap-5 md:grid-cols-3">
      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <Coins class="mr-2 w-4" /> Market Cap
          </span>
          <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
        </h2>
        <div class="flex items-center justify-between mt-6">
          <span v-if="loadingOverview" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin" /> Loading...
          </span>
          <span v-else class="text-2xl font-bold">{{ overview?.marketcap }}</span>
        </div>
      </div>

      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <TrendingUp class="mr-2 w-4" /> 24h Volume
          </span>
          <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
        </h2>
        <div class="flex items-center justify-between mt-6">
          <span v-if="loadingOverview" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin" /> Loading...
          </span>
          <span v-else class="text-2xl font-bold">{{ overview?.volume }}</span>
        </div>
      </div>

      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <Percent class="mr-2 w-4" /> Dominance
          </span>
          <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
        </h2>
        <div class="flex items-center justify-between mt-6">
          <span v-if="loadingOverview" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin" /> Loading...
          </span>
          <span v-else class="text-2xl font-bold flex gap-1">
            BTC<div class="text-muted-foreground mr-2">{{ overview?.btc_dom }}</div>
            ETH<div class="text-muted-foreground">{{ overview?.eth_dom }}</div>
          </span>
        </div>
      </div>
    </div>

    <!-- Quotes -->
    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4 flex flex-col">
      <div class="flex items-center gap-1">
        <DollarSign class="w-4" />
        <h2 class="text-sm font-semibold">Quotes</h2>
      </div>

      <div v-if="loadingOverview" class="flex items-center gap-1 text-xs text-muted-foreground">
        <LoaderCircleIcon class="size-3 animate-spin" /> Loading...
      </div>

      <Quotation v-else :data="quotation" :columns="[
        { key: 'market_cap_rank', label: '#', align: 'left' },
        { key: 'display_name', label: 'Crypto', align: 'left' },
        { key: 'price', label: 'Price', align: 'left' },
        { key: 'high_24h', label: 'High 24h', align: 'left' },
        { key: 'low_24h', label: 'Low 24h', align: 'left' },
        { key: 'price_change_24h', label: 'Change 24h', align: 'left' },
        { key: 'price_change_percentage_24h', label: 'Change %', align: 'left' },
        { key: 'market_cap', label: 'Market Cap', align: 'left' },
        { key: 'volume', label: 'Volume 24h', align: 'left' },
        { key: 'circulating_supply', label: 'Supply', align: 'left' }
      ]" />
    </div>

    <!-- Price Time Series -->
    <div class="min-h-[50vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4 flex flex-col">
      <div class="flex items-center gap-2">
        <TrendingUp class="w-4" />
        <h2 class="text-sm font-semibold">Price Time Series</h2>
      </div>

      <div v-if="loadingChart" class="flex items-center gap-1 text-xs text-muted-foreground">
        <LoaderCircleIcon class="size-3 animate-spin" /> Loading chart...
      </div>

      <div v-else>
        <p class="text-sm flex items-center text-muted-foreground mt-2">
          <CalendarSearch class="w-4 mr-2" />
          Choose a cryptocurrency and period (in days)
        </p>

        <Separator class="my-4" />

        <div class="flex h-7 items-center justify-center space-x-6 text-sm">
          <Toggle v-for="coin in quotation" :key="coin.name" :model-value="selectedCoins.includes(coin.name)"
            @update:model-value="checked => {
              if (checked && !selectedCoins.includes(coin.name)) selectedCoins.push(coin.name)
              if (!checked) selectedCoins = selectedCoins.filter(c => c !== coin.name)
            }" :disabled="isDisabledCrypto(coin.name)" class="rounded-xl cursor-pointer" aria-label="Toggle">
            <img v-if="coin.logo" :src="coin.logo" :alt="coin.display_name" class="w-4 h-4" />
            <span>{{ coin.symbol }}</span>
          </Toggle>

          <Separator orientation="vertical" />

          <Toggle v-for="num in chartDays" :key="num" :model-value="selectedDay === num"
            @update:model-value="checked => selectedDay = checked ? num : null" :disabled="isDisabledDay(num)"
            class="rounded-xl cursor-pointer border" aria-label="Toggle">
            <span>{{ num }}</span>
          </Toggle>
        </div>

        <Separator class="my-4" />

        <LineChart
          :data="chartData"
          index="date"
          :categories="chartCategories"
          :y-formatter="(tick) => `$${tick.toLocaleString()}`"
          :x-formatter="(tick: any) => tick"
        />
      </div>
    </div>
  </div>
</template>
