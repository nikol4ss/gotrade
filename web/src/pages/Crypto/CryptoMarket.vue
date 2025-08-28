<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

import {
  Coins,
  Percent,
  DollarSign,
  TrendingUp,
  LoaderCircleIcon,
  CircleQuestionMark,
} from 'lucide-vue-next'

import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/components/ui/hover-card'
import { Toggle } from '@/components/ui/toggle'
import { Separator } from '@/components/ui/separator'

import Quotation from '@/components/charts/Quotation.vue'
import LineChart from '@/components/charts/LineChart.vue'

import {
  getApiCoinGeckoOverview,
  getApiCoinGeckoTopCoins,
  getApiCoinGeckoMarketChart,
} from '@/services/api.coingecko.services'

import type {
  CoinGeckoCoin,
  CoinGeckoOverview,
  CoinGeckoMarketChart,
} from '@/models/api.coingecko.models'

const overview = ref<CoinGeckoOverview>()
const quotation = ref<CoinGeckoCoin[]>([])
const marketChart = ref<CoinGeckoMarketChart>()
const loading = ref(true)

interface ChartData {
  [key: string]: number | string
}

const chartData = computed<ChartData[]>(() => {
  if (!marketChart.value) return []
  return marketChart.value.prices.map(p => ({
    year: p.date,
    BTC: Number(p.price.replace(/[$,]/g, '')),
  }))
})

const chartCategories = ['BTC']
const numbers = [20, 40, 60, 80, 100]

onMounted(async () => {
  try {
    const [overviewData, quotationData] = await Promise.all([
      getApiCoinGeckoOverview(),
      getApiCoinGeckoTopCoins(),
    ])

    const [marketChartData] = await Promise.all([
      getApiCoinGeckoMarketChart('bitcoin', 5),
    ])

    overview.value = overviewData
    quotation.value = quotationData
    marketChart.value = marketChartData
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="flex flex-1 flex-col gap-5 p-2 pt-0">
    <div class="grid auto-rows-min gap-5 md:grid-cols-3">
      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <Coins class="mr-2 w-4" />
            Market Cap
          </span>
          <HoverCard>
            <HoverCardTrigger>
              <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
            </HoverCardTrigger>
            <HoverCardContent class="text-xs text-justify text-muted-foreground">
              Total value of all cryptocurrencies in circulation, representing the combined market capitalization.
            </HoverCardContent>
          </HoverCard>
        </h2>
        <div class="flex items-center justify-between mt-6">
          <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin " />
            Fetching updated data
          </div>
          <span v-else class="text-2xl font-bold">{{ overview?.marketcap }}</span>
        </div>
      </div>

      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <TrendingUp class="mr-2 w-4" />
            24h Volume
          </span>
          <HoverCard>
            <HoverCardTrigger>
              <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
            </HoverCardTrigger>
            <HoverCardContent class="text-xs text-justify text-muted-foreground">
              Total value of all cryptocurrency transactions executed in the past 24 hours across the market.
            </HoverCardContent>
          </HoverCard>
        </h2>
        <div class="flex items-center justify-between mt-6">
          <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin" />
            Fetching updated data
          </div>
          <span v-else class="text-2xl font-bold">{{ overview?.volume }}</span>
        </div>
      </div>

      <div class="rounded-xl bg-muted/50 p-3 flex flex-col">
        <h2 class="text-sm font-medium flex items-center justify-between">
          <span class="flex items-center">
            <Percent class="mr-2 w-4" />
            Dominance
          </span>
          <HoverCard>
            <HoverCardTrigger>
              <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
            </HoverCardTrigger>
            <HoverCardContent class="text-xs text-justify text-muted-foreground">
              Percentage share of each leading cryptocurrency in the total market capitalization.
            </HoverCardContent>
          </HoverCard>
        </h2>
        <div class="flex items-center justify-between mt-6">
          <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
            <LoaderCircleIcon class="size-3 animate-spin" />
            Fetching updated data
          </div>
          <span v-else class="text-2xl font-bold flex gap-1">
            BTC<div class="text-muted-foreground mr-2">{{ overview?.btc_dom }}</div>
            ETH<div class="text-muted-foreground">{{ overview?.eth_dom }}</div>
          </span>
        </div>
      </div>
    </div>

    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4 flex flex-col">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-1 ">
          <DollarSign class=" w-4" />
          <h2 class="text-sm font-semibold">Quotes</h2>
        </div>
        <HoverCard>
          <HoverCardTrigger>
            <CircleQuestionMark class="w-4 cursor-help text-muted-foreground" />
          </HoverCardTrigger>
          <HoverCardContent class="text-xs text-justify text-muted-foreground">
            This table shows key data for each cryptocurrency, including rank,
            name, price, daily range, performance, market cap, trading volume,
            and circulating supply.
          </HoverCardContent>
        </HoverCard>
      </div>

      <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
        <LoaderCircleIcon class="size-3 animate-spin" />
        Fetching updated data
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

    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4 flex flex-col">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-4" />
        <h2 class="text-sm font-semibold">Price Time Series</h2>
      </div>

      <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
        <LoaderCircleIcon class="size-3 animate-spin" />
        Fetching updated data
      </div>

      <div class="flex items-center">
        <div>
          <div class="space-y-1">
            <p class="text-sm text-muted-foreground">
              An open-source UI component library.
            </p>
          </div>
          <Separator class="my-4" />
          <div class="flex h-5 items-center space-x-4 text-sm">
            <Toggle v-for="coin in quotation" :key="coin.name" :value="coin.name" aria-label="Toggle"
              class="rounded-xl ml-2">
              <img v-if="coin.logo" :src="coin.logo" :alt="coin.display_name" class="w-4 h-4 " />
              <span>{{ coin.symbol }}</span>
            </Toggle>

            <Separator orientation="vertical" />

            <Toggle v-for="num in numbers" :key="num" :value="num" aria-label="Toggle" class="rounded-xl ml-3 border">
              <span>{{ num }}</span>
            </Toggle>
          </div>
          <Separator class="my-4" />
        </div>
      </div>

      <div class="flex justify-center pr-5">
        <LineChart :data="chartData" index="year" :categories="chartCategories"
          :y-formatter="(tick) => `$${tick.toLocaleString()}`" class="w-full" />
      </div>
    </div>
  </div>
</template>
