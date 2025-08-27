<script setup lang="ts">
import { onMounted, ref } from 'vue';

import {
  Coins,
  Percent,
  DollarSign,
  TrendingUp,
  LoaderCircleIcon,
  CircleQuestionMark,
} from 'lucide-vue-next';

import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/components/ui/hover-card'

import Quotation from '@/components/charts/Quotation.vue';

import { getApiCoinGeckoOverview, getApiCoinGeckoTopCoins } from '@/services/api.coingecko.services';
import type { CoinGeckoCoin, CoinGeckoOverview } from '@/models/api.coingecko.models';


const quotation = ref<CoinGeckoCoin[]>([]);
const overview = ref<CoinGeckoOverview>();

const loading = ref(true);

onMounted(async () => {
  try {
    const [overviewData, quotationData] = await Promise.all([
      getApiCoinGeckoOverview(),
      getApiCoinGeckoTopCoins()
    ]);
    overview.value = overviewData;
    quotation.value = quotationData;
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="flex flex-1 flex-col gap-5 p-2 pt-0">
    <div class="grid auto-rows-min gap-5 md:grid-cols-3">

      <!-- Overview -->
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

    <!-- Quotes -->
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

    <!-- Price Time Series -->
    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4 flex flex-col">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-4" />
        <h2 class="text-sm font-semibold">Price Time Series</h2>
      </div>

      <div v-if="loading" class="flex items-center gap-1 text-xs text-muted-foreground">
        <LoaderCircleIcon class="size-3 animate-spin" />
        Fetching updated data
      </div>

      <div>
        <!-- <LineChart :data="priceHistoryData" :categories="['BTC', 'ETH', 'SOL']" :colors="['blue', 'green', 'orange']" -->
        <LineChart :categories="['BTC', 'ETH', 'SOL']" :colors="['blue', 'green', 'orange']" class="" />
      </div>
    </div>

  </div>

</template>
