<script setup lang="ts">
import {
  DollarSign,
  TrendingUp,
  Activity,
  AlertCircle,
  Star,
  BookOpen,
  Coins,
  Percent,
} from 'lucide-vue-next';

import AreaChart from '@/components/charts/AreaChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
// import DonutChart from '@/components/charts/DonutChart.vue';
import BarChart from '@/components/charts/BarChart.vue';
import Quotation from '@/components/charts/Quotation.vue';

import { getApiCoinGeckoOverview, getApiCoinGeckoTopCoins } from '@/services/api.coingecko.services';
import type { CoinQuotationModel } from '@/models/api.coingecko.models';

import { onMounted, ref } from 'vue';

const quotation = ref<CoinQuotationModel[]>([]);

const overview = ref<null | {
  marketcap: string
  volume: string
  btc_dom: string
  eth_dom: string
}>(null)

const priceHistoryData = [
  { name: "Jan", BTC: 30000, ETH: 2000, SOL: 150 },
  { name: "Feb", BTC: 31000, ETH: 2100, SOL: 155 },
  { name: "Mar", BTC: 29000, ETH: 1900, SOL: 145 },
  { name: "Apr", BTC: 31500, ETH: 2200, SOL: 165 },
];

const indicatorsData = [
  { indicator: "RSI BTC", value: 62, status: "Neutral" },
  { indicator: "MACD BTC", value: "+150", status: "Bullish" },
  { indicator: "SMA 50 BTC", value: "29.500", status: "Above trend" },
  { indicator: "RSI ETH", value: 58, status: "Neutral" },
];

const alertsData = [
  "RSI sobrecompra BTC",
  "Volatilidade ETH alta",
  "Queda brusca de volume SOL"
];

const topVolume = [
  { name: "BTC", volume: 35 },
  { name: "ETH", volume: 18 },
  { name: "SOL", volume: 1.2 },
  { name: "ADA", volume: 0.9 },
];

const marketStats = {
  marketCap: "1.15T",
  volume24h: "85B",
  activeCryptos: 4500,
  btcDominance: "48.2%",
  ethDominance: "17.4%",
};

const converterData = [
  { pair: "BTC/USD", rate: 30250 },
  { pair: "ETH/BTC", rate: 0.0677 },
  { pair: "SOL/BTC", rate: 0.006 }
];

const yFormatter = (tick: number | Date) =>
  typeof tick === "number" ? `$ ${new Intl.NumberFormat("us").format(tick)}` : tick.toString();

async function showOverview() {
  overview.value = await getApiCoinGeckoOverview();
}

async function showQuotation() {
  quotation.value = await getApiCoinGeckoTopCoins();
}

onMounted(async () => {
  showOverview()
  showQuotation()
});
</script>

<template>
  <div class="flex flex-col gap-6 p-2">
    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
        <h2 class=" text-base font-medium flex items-center">
          <Coins class="mr-2 w-4" />Market Cap
        </h2>
        <span class="text-2xl font-bold mt-3">{{ overview?.marketcap }}</span>
        <span class="text-xs mt-1 text-muted-foreground">Cryptocurrency total market cap</span>
      </div>
      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
        <h2 class="text-base font-medium flex items-center">
          <TrendingUp class="mr-2 w-4" />24h Trading Volume
        </h2>
        <span class="text-2xl font-bold mt-3">{{ overview?.volume }}</span>
        <span class="text-xs mt-1 text-muted-foreground">Total traded in the last 24 hours</span>
      </div>
      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
        <h2 class="text-base font-medium flex items-center">
          <Percent class="mr-2 w-4" />Market Dominance
        </h2>
        <span class="text-2xl font-bold mt-3">BTC {{ overview?.btc_dom }} ETH {{ overview?.eth_dom
          }}</span>
        <span class="text-xs mt-1 text-muted-foreground">Share of top cryptocurrencies in the market</span>
      </div>
    </div>

    <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <DollarSign class=" w-4" />
        <h2 class="text-base font-semibold">Crypto Quotes</h2>
      </div>
      <Quotation :data="quotation" :columns="[
        { key: 'display_name', label: 'Cryptocurrency', align: 'left' },
        { key: 'price', label: 'Price (USD)', align: 'center' },
        { key: 'market_cap', label: 'Market Cap', align: 'right' },
        { key: 'volume', label: '24h Volume', align: 'right' },
        { key: 'price_change_percentage_24h', label: 'Change 24h (%)', align: 'center' },
        { key: 'price_change_24h', label: 'Change 24h (USD)', align: 'center' },
        { key: 'high_24h', label: '24h High', align: 'right' },
        { key: 'low_24h', label: '24h Low', align: 'right' },
        { key: 'circulating_supply', label: 'Circulating Supply', align: 'right' }
      ]" />



    </div>


    <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-4" />
        <h2 class="text-base font-semibold">Multi-Cryptocurrency Price History</h2>
      </div>
      <div>
        <LineChart :data="priceHistoryData" :categories="['BTC', 'ETH', 'SOL']" :colors="['blue', 'green', 'orange']"
          :y-formatter="yFormatter" class="" />
      </div>
    </div>

    <!-- Linha 3: Indicadores + Alertas -->
    <div class="grid gap-6 md:grid-cols-2">
      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <Activity class="w-5 h-5" />
          <h2 class="text-lg font-semibold">Indicadores Técnicos</h2>
        </div>
        <ul class="text-sm text-muted-foreground space-y-1">
          <li v-for="item in indicatorsData" :key="item.indicator">
            {{ item.indicator }}: <span class="font-medium">{{ item.value }}</span> ({{ item.status }})
          </li>
        </ul>
      </div>

      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <AlertCircle class="w-5 h-5" />
          <h2 class="text-lg font-semibold">Alertas Preventivos</h2>
        </div>
        <ul class="text-sm text-muted-foreground space-y-1">
          <li v-for="alert in alertsData" :key="alert">{{ alert }}</li>
        </ul>
      </div>
    </div>

    <!-- Linha 4: Tendência Consolidada -->
    <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-5 h-5" />
        <h2 class="text-lg font-semibold">Tendência Consolidada</h2>
      </div>
      <AreaChart :data="priceHistoryData" :categories="['BTC', 'ETH', 'SOL']" :colors="['blue', 'green', 'orange']"
        :y-formatter="yFormatter" class="flex-1 w-full h-96" />
    </div>

    <!-- Linha 5: Volume (BarChart grande) -->
    <div class="rounded-2xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <Star class="w-5 h-5" />
        <h2 class="text-lg font-semibold">Top Criptos por Volume</h2>
      </div>
      <BarChart :data="topVolume" :categories="['volume']" :colors="['blue']" :y-formatter="yFormatter"
        class="flex-1 w-full h-96" />
    </div>

    <!-- Linha 6: Conversor + Métricas Rápidas -->
    <div class="grid gap-6 md:grid-cols-2">
      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <DollarSign class="w-5 h-5" />
          <h2 class="text-lg font-semibold">Conversor de Cripto</h2>
        </div>
        <ul class="text-sm text-muted-foreground space-y-1">
          <li v-for="pair in converterData" :key="pair.pair">{{ pair.pair }} → <span class="font-medium">{{ pair.rate
              }}</span></li>
        </ul>
      </div>

      <div class="rounded-2xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <BookOpen class="w-5 h-5" />
          <h2 class="text-lg font-semibold">Notícias & Métricas</h2>
        </div>
        <span class="text-sm text-muted-foreground">Últimas análises, hype coins, alertas institucionais e métricas
          rápidas de mercado</span>
        <ul class="text-sm text-muted-foreground space-y-1 mt-2">
          <li>Market Cap: <span class="font-medium">{{ marketStats.marketCap }}</span></li>
          <li>Volume 24h: <span class="font-medium">{{ marketStats.volume24h }}</span></li>
          <li>Criptos Ativas: <span class="font-medium">{{ marketStats.activeCryptos }}</span></li>
          <li>BTC Dominance: <span class="font-medium">{{ marketStats.btcDominance }}</span></li>
          <li>ETH Dominance: <span class="font-medium">{{ marketStats.ethDominance }}</span></li>
        </ul>
      </div>
    </div>
  </div>
</template>
